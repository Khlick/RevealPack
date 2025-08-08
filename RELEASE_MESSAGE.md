# RevealPack v1.3.7

## 🚀 New Features

### Enhanced Plugin Parsing

This release introduces powerful new plugin configuration options that give you fine-grained control over how plugins are processed in your Reveal.js presentations.

#### New Plugin Fields

**`noscript` Field**
- When set to `true`, prevents the plugin script tag from being generated in the HTML template
- Perfect for analytics plugins, utility libraries, or custom initialization scripts
- Plugin files are still downloaded and copied, but no `<script>` tag is created

**`omit` Field**
- When set to `true`, prevents the plugin from being listed in the Reveal.js plugin list
- Ideal for background services, auto-initializing plugins, or legacy compatibility
- Script tag is still generated, but plugin won't appear in `plugins: []` array

#### Usage Examples

```json
{
  "packages": {
    "reveal_plugins": {
      "external": {
        "analytics": {
          "version": "1.0.0",
          "alias": "analytics-plugin",
          "main": "analytics-main",
          "export": "Analytics",
          "noscript": true,
          "omit": false
        },
        "tracking": {
          "version": "1.0.0",
          "alias": "tracking-plugin",
          "main": "tracking-main",
          "export": "Tracking",
          "noscript": false,
          "omit": true
        }
      }
    }
  }
}
```

### Enhanced MathJax Processing

Flexible MathJax version specification with support for multiple versions using the `mathjax#` pattern.

#### Supported Patterns

- `mathjax` → `RevealMath`
- `mathjax2` → `RevealMath.MathJax2`
- `mathjax3` → `RevealMath.MathJax3`
- `mathjax4` → `RevealMath.MathJax4`

#### Configuration Example

```json
{
  "packages": {
    "reveal_plugins": {
      "built_in": ["math"],
      "plugin_configurations": {
        "mathjax4": {
          "mathjax": "https://cdn.jsdelivr.net/npm/mathjax@4.0.0-beta.6/tex-mml-chtml.js"
        }
      }
    }
  }
}
```

## 🔧 Improvements

- **Backward Compatibility**: All existing configurations continue to work unchanged
- **Flexible Configuration**: New fields are optional and default to `false`
- **No Validation**: MathJax version numbers are not strictly validated as requested
- **Clean Implementation**: Built-in plugins are not affected by the new fields

## 📚 Documentation

- Updated configuration documentation with comprehensive examples
- Added detailed use cases for each new feature
- Enhanced examples showing real-world plugin configurations
- Improved MathJax processing documentation

## 🐛 Bug Fixes

- Fixed plugin parsing logic for built-in vs external plugins
- Corrected template generation for plugin script tags
- Improved MathJax version detection and processing

## 🔄 Migration

No migration required! All existing configurations will continue to work as before. The new fields are optional and only need to be added when you want to use the new functionality.

## 📦 Installation

```bash
pip install revealpack==1.3.7
```

## 🎯 Use Cases

### `noscript` Use Cases
- **Analytics plugins**: Include analytics code without Reveal.js plugin overhead
- **Utility libraries**: Libraries that provide global functionality
- **Custom initialization**: Scripts that need to be loaded but initialized separately

### `omit` Use Cases
- **Background services**: Plugins that run in the background
- **Auto-initializing plugins**: Plugins that automatically initialize themselves
- **Legacy compatibility**: Plugins that might conflict with explicit listing

### MathJax Use Cases
- **Version flexibility**: Easy switching between MathJax versions
- **Future compatibility**: Support for upcoming MathJax versions
- **Configuration simplicity**: No need to manually specify the correct plugin name

---

**Full Changelog**: See the commit history for detailed changes.
