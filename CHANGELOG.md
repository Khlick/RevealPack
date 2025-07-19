# Changelog

All notable changes to RevealPack will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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