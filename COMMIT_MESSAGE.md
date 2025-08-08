feat: enhance plugin parsing with noscript/omit fields and flexible MathJax processing

- Add `noscript` field to external plugins to prevent script tag generation
- Add `omit` field to external plugins to exclude from Reveal.js plugin list
- Implement enhanced MathJax processing with flexible `mathjax#` pattern support
- Support MathJax versions: mathjax, mathjax2, mathjax3, mathjax4
- Update documentation with examples and use cases for new features
- Fix plugin parsing logic for built-in vs external plugins
- Maintain backward compatibility with existing configurations

Breaking Changes: None
New Features:
- Plugin noscript/omit control fields
- Flexible MathJax version specification
- Enhanced plugin configuration options

Documentation:
- Updated config.md with new field descriptions
- Added Enhanced MathJax Processing section
- Updated example.md with new plugin configurations

Version: 1.3.7
