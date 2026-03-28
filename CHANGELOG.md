# Changelog

All notable changes to RevealPack will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.6.0] - 2026-03-27

### Added
- **Per-deck Reveal plugins** via `presentation.json` → **`plugins`**:
  - **`reveal`**: array of `{ "name": "..." }` entries (e.g. `markdown`, `mathjax4`). Names are resolved to filesystem bundles under cached reveal.js and to JS identifiers (`RevealMarkdown`, `RevealMath.MathJax4`, etc.); invalid names are skipped with a warning.
  - **`external`**: array of `{ "name": "...", "source": "https://..." }` for CDN scripts; **source** is the URL in the generated `<script>` tag.
  - Optional **`config`** on each `reveal` / `external` entry: `{ "config_id": "chalkboard", "settings": { ... } }` → emitted in `Reveal.initialize` after `plugins: [...]` (same JS object style as global `plugin_configurations`).

### Changed
- `reveal_template.html` injects `{{ reveal_plugins_list_js }}` and `{{ deck_plugin_config_js }}` (built in Python); deck `plugins.reveal` / `plugins.external` are normalized with `slug`, `js_id`, and validated **source**.
- **`copy_plugins()`** unions filesystem slugs required by deck `plugins.reveal` (after validation) with global `built_in` plugins.

### Technical Details
- `revealpack/_utils/reveal_plugin_helpers.py` (resolution, cache checks, `prepare_deck_plugins`); updates to `revealpack/setup.py` and `revealpack/build.py`; `docs/presentation.md`.

## [1.5.0] - 2026-03-27

### Added
- **Reveal.js 6.x support** alongside existing **5.x** support: setup and build detect the cached Reveal major version and adjust built-in plugin copy paths, highlight theme locations, and generated `<script src>` paths (flat `dist/plugin/<name>.js` for 6.x vs nested `plugin/<name>/` for 5.x).
- **Config vs cache warning**: `revealpack build` logs a warning when `packages.reveal.js` disagrees with `source/cached/reveal.js/package.json`, prompting a refresh with `revealpack setup --force-plugin-download`.

### Changed
- **Default new projects** (`revealpack init`): Reveal.js **6.0.0**, MathJax **4.1.1** via `plugin_configurations.mathjax4` (including CDN URL `mathjax@4.1.1`).
- **Documentation** updated for 5.x vs 6.x plugin layout, supported versions (minimum Reveal **5.0**), and refreshed examples across README and `docs/`.
- **`revealpack/config.json`**: aligned with new defaults; fixed typo `directories.pacakge` → `package`.

### Fixed
- **Build logging**: project title log line no longer relies on nested double quotes inside an f-string (broader Python compatibility).

### Technical Details
- Modified `revealpack/setup.py` (`parse_reveal_js_major_version`, template plugin and highlight paths), `revealpack/build.py` (`load_revealjs_major_version`, `copy_plugins`, `copy_reveal`, `compile_theme` / highlight helpers, `warn_reveal_config_cache_mismatch`), and `revealpack/__init__.py` (`generate_config`).

## [1.4.8] - 2025-02-24

### Added
- **Optional favicon configuration**: New `favicon` option in `config.json` to control favicon inclusion in generated templates.
  - When set to a path (e.g. `"favicon.png"` or `"favicon.ico"`), the path is interpreted relative to the libraries directory; the favicon `<link>` is included in both the reveal template and the TOC template.
  - When `null` or omitted, no favicon link is emitted in either template.
  - Default generated config includes `"favicon": null`.

### Technical Details
- Modified `revealpack/setup.py`: `create_reveal_template()` and `create_toc_template()` now conditionally add the favicon `<link>` based on `config.get("favicon")`.
- Updated `revealpack/__init__.py` default config and `revealpack/config.json` to include the optional `favicon` key.

## [1.4.7] - 2024-12-19

### Fixed
- **Highlight.js Theme Handling**: Fixed issue where setup would fail when `highlight_theme` config option was set but the CSS file wasn't found
  - Initialized `highlight_css` variable before the file search loop to prevent `NameError`
  - Changed condition check from truthy evaluation to explicit `is not None` check
  - Added proper fallback HTML comment when highlight theme CSS is not found
  - Setup now gracefully handles missing highlight theme files and defaults to 'monokai' with appropriate warning

### Technical Details
- Modified `revealpack/setup.py` in `create_reveal_template()` function
- Improved error handling for highlight.js theme configuration
- All changes maintain backward compatibility

## [1.4.6] - 2024-12-19

### Fixed
- **Critical Newline Issue**: Fixed HTML parsing that was adding extra blank lines between code block lines
  - Resolved issue where `\n` was being interpreted as `\n\n` in HTML slide content
  - Code blocks now maintain proper formatting without extra blank lines
  - highlight.js will parse code correctly without spacing issues
  - Improved HTML beautification to preserve exact code block formatting

### Technical Details
- Modified `revealpack/_utils/presentation_operations.py` to fix newline handling in `parse_slide` function
- Enhanced `revealpack/_utils/html_operations.py` to better preserve code block HTML content
- Fixed root cause where `readlines()` + `"\n".join()` was creating double newlines
- All changes maintain backward compatibility and improve code block rendering quality

## [1.4.5] - 2024-12-19

### Changed
- **Dependency Cleanup**: Optimized package dependencies for better user experience
  - Removed unused `flask` dependency that was not being utilized
  - Moved `mkdocs` and `mkdocs-material` to development dependencies
  - Reduced package size for end users while maintaining all functionality
  - Documentation building capabilities preserved for development workflows

### Technical Details
- Modified `pyproject.toml` to remove unused runtime dependencies
- Moved documentation build tools to appropriate dev dependency section
- All core functionality remains unchanged and backward compatible
- Package is now lighter and more focused on essential runtime requirements

## [1.4.4] - 2024-12-19

### Fixed
- **Logging Configuration**: Fixed issue where logging level set in `config.json` was being ignored
  - Modified `initialize_logging` function to properly set root logger level
  - Ensures logging configuration from config file is always respected
  - Improved handler management for consistent logging behavior
- **Unicode Encoding**: Fixed `UnicodeEncodeError` when writing HTML files with special characters
  - Added `encoding="utf-8"` to all file operations throughout the codebase
  - Resolves issues with characters like '\u2753' that couldn't be encoded in Windows-1252
  - Ensures proper handling of international characters and emojis in presentations

### Technical Details
- Modified `revealpack/_utils/config_operations.py` for proper logging initialization
- Updated file operations in `revealpack/build.py`, `revealpack/package.py`, `revealpack/setup.py`, `revealpack/__init__.py`, and `revealpack/_utils/file_operations.py`
- All changes maintain backward compatibility and improve cross-platform reliability

## [1.4.1] - 2024-12-19

### Security
- **Enhanced Tar Extraction Security**: Added `filter='data'` argument to all `tar.extractall()` calls
- Prevents path traversal attacks through malicious tar archives
- Eliminates deprecation warnings for Python 3.14 compatibility
- Improves security when downloading and extracting external plugins

### Technical Details
- Modified `revealpack/setup.py` to use secure tar extraction methods
- All tar archive extractions now explicitly filter for data files only
- Maintains backward compatibility while improving security posture

## [1.4.0] - 2024-12-19

### Fixed
- **Critical Bug Fix**: Fixed Jinja2 whitespace stripping that was destroying code block formatting in presentations
- Users no longer need to use HTML entities like `&#9;` for tabs in code blocks
- Code blocks now maintain proper indentation and structure during build process

### Added
- **New Build Settings Configuration**: Added `build_settings` section to `config.json`
  - `preserve_code_formatting`: Controls whitespace preservation in code blocks (default: `true`)
  - `html_indent_size`: Controls HTML indentation size (default: `2`)
- **Enhanced HTML Beautification**: Improved `beautify_html` function to intelligently preserve code formatting
- **Better Asset Management**: Enhanced asset copying with improved exclusion patterns and recursive handling

### Changed
- **Jinja2 Environment**: Modified template rendering to preserve code formatting by default
- **Build Process**: Code formatting preservation is now enabled by default for better user experience
- **Configuration**: New build settings provide granular control over formatting behavior

### Technical Details
- Modified `revealpack/build.py` to respect `build_settings.preserve_code_formatting`
- Enhanced `revealpack/_utils/html_operations.py` with smart code block preservation
- Updated documentation in `docs/config.md` with new configuration options
- All changes are backward compatible with existing presentations

## [1.3.7] - 2024-12-19

### Added
- **Enhanced Plugin Configuration**: Added support for `noscript` and `omit` fields in plugin configurations
  - `noscript`: Allows plugins to be loaded without JavaScript wrapper
  - `omit`: Enables conditional plugin loading based on configuration
- **Flexible MathJax Processing**: Improved handling of MathJax configurations
  - Better support for custom MathJax configurations
  - More reliable loading of MathJax components
  - Enhanced error handling for MathJax initialization

### Changed
- **Plugin Loading System**: Refactored plugin loading mechanism
  - More granular control over how plugins are included
  - Improved error handling for plugin loading failures
  - Better support for plugins with special loading requirements

### Technical Details
- Modified plugin parsing logic in `revealpack/build.py`
- Enhanced MathJax configuration handling in templates
- Updated documentation to reflect new plugin configuration options
- All changes maintain backward compatibility with existing presentations

## [1.3.6] - 2024-12-19

### Fixed
- Resolved path handling issues in Windows environments
- Fixed plugin dependency resolution order

## [1.3.5] - 2024-12-19

### Added
- Better error messages for plugin loading failures
- Improved logging for build process

## [1.3.4] - 2024-12-19

### Fixed
- Corrected plugin path resolution for nested configurations
- Fixed CSS loading order issues

## [1.3.3] - 2024-12-19

### Changed
- Optimized plugin loading performance
- Improved error handling for malformed plugin configurations


## [1.3.2] - 2024-12-19

### Fixed
- 1.3.1 introduced scss into revealpack.scss that had undefined variables, removed these.

## [1.3.1] - 2024-12-19

### Added
- Enhanced print functionality with `print-invisible` CSS class
- Support for `?print-pdf+show` URL parameter to show hidden elements in print mode
- JavaScript logic to parse URL parameters and inject appropriate CSS rules
- Comprehensive documentation for print functionality across README, template.md, styles.md, and example.md

### Changed
- Updated Reveal.js template to include enhanced print logic
- Improved print CSS handling with dynamic stylesheet injection

### Technical Details
- Added `print-invisible` class to revealpack.scss with `visibility: hidden !important`
- Implemented JavaScript to detect `+show` parameter and override print-invisible styles
- Enhanced template generation in setup.py to include new print functionality

## [1.3.0] - Previous Release

Initial stable release with core functionality including:
- Multi-presentation management
- Shared resources and themes
- SCSS/SASS compilation
- Plugin management
- Distribution packaging
- Live development server 