"""Reveal.js plugin names, deck plugin resolution, and cache validation."""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any


def mathjax_plugin_identifier(config: dict) -> str:
    """Reveal.initialize identifier for global `math` built-in from plugin_configurations."""
    plugin_config = config["packages"]["reveal_plugins"].get("plugin_configurations", {})

    for key in plugin_config.keys():
        if key.startswith("mathjax"):
            version = key[7:] if len(key) > 7 else ""
            if version in ["", "2", "3", "4"]:
                return f"RevealMath.MathJax{version}" if version else "RevealMath"

    if "mathjax2" in plugin_config:
        return "RevealMath.MathJax2"
    if "mathjax3" in plugin_config:
        return "RevealMath.MathJax3"
    if "mathjax4" in plugin_config:
        return "RevealMath.MathJax4"
    if "katex" in plugin_config:
        return "RevealMath.KaTeX"
    return "RevealMath"


def global_plugin_names_for_initialize(config: dict) -> str:
    """Comma-separated plugin identifiers for config.json global plugins."""
    builtin_plugins = config["packages"]["reveal_plugins"]["built_in"]
    external_plugins = config["packages"]["reveal_plugins"].get("external", {})

    names: list[str] = []
    for plugin in builtin_plugins:
        names.append(f"Reveal{plugin.capitalize()}")

    if "RevealMath" in names:
        names[names.index("RevealMath")] = mathjax_plugin_identifier(config)

    for plugin, details in external_plugins.items():
        if details.get("omit", False):
            continue
        names.append(details.get("export", plugin.capitalize()))

    return ", ".join(names)


def resolve_reveal_plugin_name(name: str, config: dict) -> tuple[str, str]:
    """Map presentation `plugins.reveal[].name` to (filesystem bundle slug, JS identifier)."""
    n = str(name).strip().lower()
    if n == "math":
        return "math", mathjax_plugin_identifier(config)
    if n in ("mathjax", "mathjax1"):
        return "math", "RevealMath"
    if n == "mathjax2":
        return "math", "RevealMath.MathJax2"
    if n == "mathjax3":
        return "math", "RevealMath.MathJax3"
    if n == "mathjax4":
        return "math", "RevealMath.MathJax4"
    if n == "katex":
        return "math", "RevealMath.KaTeX"
    return n, f"Reveal{n.capitalize()}"


def reveal_plugin_bundle_exists(reveal_root: Path, major: int, slug: str) -> bool:
    """True if the bundled plugin exists under cached reveal.js (matches copy_plugins layout)."""
    if major >= 6:
        base = reveal_root / "dist" / "plugin"
        if (base / f"{slug}.js").is_file():
            return True
        if (base / slug).is_dir():
            return True
        return False
    return (reveal_root / "plugin" / slug).is_dir()


def deck_reveal_slugs_for_copy(
    presentation_root: str, config: dict, reveal_root: Path, major: int
) -> set[str]:
    """Filesystem slugs needed by any deck `plugins.reveal` entry (validated against cache)."""
    slugs: set[str] = set()
    if not presentation_root or not os.path.isdir(presentation_root):
        return slugs

    for entry in os.listdir(presentation_root):
        deck_dir = os.path.join(presentation_root, entry)
        if not os.path.isdir(deck_dir):
            continue
        pj = os.path.join(deck_dir, "presentation.json")
        if not os.path.exists(pj):
            continue
        try:
            with open(pj, encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            logging.warning("Could not read %s: %s", pj, e)
            continue
        for item in (data.get("plugins") or {}).get("reveal") or []:
            if not isinstance(item, dict):
                continue
            raw_name = item.get("name")
            if not raw_name or not isinstance(raw_name, str):
                continue
            slug, _ = resolve_reveal_plugin_name(raw_name.strip(), config)
            if reveal_plugin_bundle_exists(reveal_root, major, slug):
                slugs.add(slug)
            else:
                logging.warning(
                    "Presentation %s: reveal plugin name %r resolves to bundle %r "
                    "which is not present under cached reveal.js; build may miss files.",
                    pj,
                    raw_name,
                    slug,
                )
    return slugs


def prepare_deck_plugins(
    deck: dict, config: dict, reveal_root: Path, major: int
) -> None:
    """Normalize `deck.plugins` to `{ reveal: [{name, slug, js_id}], external: [{name, source}] }`."""
    if deck.get("deck_reveal_plugins") is not None:
        logging.warning(
            "deck_reveal_plugins is deprecated; use plugins.reveal and plugins.external instead."
        )

    raw = deck.get("plugins")
    if raw is None:
        deck["plugins"] = {"reveal": [], "external": []}
        return
    if not isinstance(raw, dict):
        logging.warning("plugins must be an object; ignoring.")
        deck["plugins"] = {"reveal": [], "external": []}
        return

    reveal_out: list[dict[str, Any]] = []
    for item in raw.get("reveal") or []:
        if not isinstance(item, dict):
            logging.warning("Skipping invalid plugins.reveal entry (not an object).")
            continue
        raw_name = item.get("name")
        if not raw_name or not isinstance(raw_name, str):
            logging.warning("Skipping plugins.reveal entry without string name: %s", item)
            continue
        slug, js_id = resolve_reveal_plugin_name(raw_name.strip(), config)
        if not reveal_plugin_bundle_exists(reveal_root, major, slug):
            logging.warning(
                "Skipping unknown reveal plugin name %r (no bundle %r under cached reveal.js).",
                raw_name.strip(),
                slug,
            )
            continue
        reveal_out.append(
            {"name": raw_name.strip(), "slug": slug, "js_id": js_id}
        )

    ext_out: list[dict[str, str]] = []
    for item in raw.get("external") or []:
        if not isinstance(item, dict):
            logging.warning("Skipping invalid plugins.external entry (not an object).")
            continue
        name = item.get("name")
        source = item.get("source")
        if not name or source is None:
            logging.warning(
                "Skipping plugins.external entry missing name or source: %s", item
            )
            continue
        ext_out.append({"name": str(name), "source": str(source)})

    deck["plugins"] = {"reveal": reveal_out, "external": ext_out}
