"""Lenient JSON parsing for hand-edited project files (e.g. trailing commas)."""

from __future__ import annotations

import json
import logging
import re
from typing import Any


def relax_json_trailing_commas(text: str) -> str:
    """Remove commas immediately before `}` or `]` (repeat for nested structures)."""
    out = text
    for _ in range(128):
        new = re.sub(r",(\s*[}\]])", r"\1", out)
        if new == out:
            break
        out = new
    return out


def json_loads_lenient(text: str, *, source: str | None = None) -> Any:
    """Parse JSON; on failure, retry after stripping illegal trailing commas (JSON5-style)."""
    try:
        return json.loads(text)
    except json.JSONDecodeError as err:
        try:
            fixed = relax_json_trailing_commas(text)
            data = json.loads(fixed)
        except json.JSONDecodeError:
            raise err
        if source:
            logging.debug(
                "Parsed JSON with trailing-comma fix: %s (prefer strict JSON without trailing commas)",
                source,
            )
        return data
