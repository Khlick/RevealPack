# Configurations

Reference the table below for configuration options parsed by the [`revealpack setup`](setup.md) command.

### Table 1. Configurations for `config.json`

| Key                      | Sub-Key                      | Description                                                                 |
|--------------------------|------------------------------|-----------------------------------------------------------------------------|
| `info`                   |                              | Information about the project                                               |
|                          | `project_title`              | The full title of your project                                              |
|                          | `short_title`                | A short, concise title for your project                                     |
|                          | `version`                    | The current version of your project                                         |
|                          | `authors`                    | An array containing the names of the authors                                |
| `directories`            |                              | Configuration for directory structure used in the project                   |
|                          | `build`                      | Directory where the built presentation will be output (e.g., `build`)       |
|                          | `package`                    | Directory for distribution of the packaged app (e.g., `dist`)               |
| `directories.source`     |                              | Root configuration for source directories                                   |
|                          | `root`                       | Root directory for all source files (e.g., `source`)                        |
|                          | `presentation_root`          | Directory for storing individual presentation decks (e.g., `decks`)         |
|                          | `libraries`                  | Directory for storing shared libraries and assets (e.g., `lib`)             |
| `packages`               |                              | Configuration for Reveal.js and associated plugins                          |
|                          | `reveal.js`                  | The version of Reveal.js to be used (e.g., `5.1.0`)                         |
| `packages.reveal_plugins`|                              | Plugins configuration for Reveal.js                                         |
|                          | `built_in`                   | List of built-in plugins to include (e.g., `notes`, `highlight`, `math`)    |
|                          | [`external`](#packagesreveal_pluginsexternal) | External plugins with their versions and download URLs     |
|                          | `plugin_configurations`      | Specific configurations for each plugin                                     |
| `theme`                  |                              | Path to the custom theme CSS file (e.g., `custom_theme/theme.css`)          |
| `reveal_template`        |                              | Name of the Jinja2 template file for generating the presentation HTML       |
| `toc_template`           |                              | Path to the Jinja2 template file for generating the table of contents HTML  |
| `logging`                |                              | Logging level for setup and build processes (e.g., `error`, see [logging docs](https://docs.python.org/3/library/logging.html#levels).) |
| `highlight_theme`        |                              | Path to the highlight.js theme CSS file (e.g., `custom_theme/hybrid.css`)   |
| [`custom_scripts`](#custom_scripts) |                   | Array of custom JavaScript files to include in the presentation             |
| `force_plugin_download`  |                              | Boolean to force re-download of plugins, even if they are already present   |
| `reveal_configurations`  |                              | Configuration options for Reveal.js (see [Reveal configuration](https://revealjs.com/config/))|
| `build_settings`         |                              | Configuration options for the build process                                  |
|                          | `preserve_code_formatting`   | Boolean to preserve whitespace in code blocks (default: true)              |
|                          | `html_indent_size`           | Number of spaces for HTML indentation (default: 2)                          |

## Specifications On Select Configurations

### `packages.reveal_plugins.external`

External plugins are optional, so the `external` field may be omitted. However, inclusion of external packages should be in the form of:
```json
{
  "packages": {
    "reveal.js": "5.1.0",
    "reveal_plugins": {
      "external": {
        "plugin1-name": {
          "version": "0.0.0",
          "url": "https://path/to/url.tar.gz"
        },
        "plugin2-name": {
          "version": "1.0.4"
        }
      }
    }
  }, // other config options
}
```
Where `url` may be omitted if the package is locatable on npm with the template:

```python
plugin_url = f"https://registry.npmjs.org/{plugin}/-/{plugin}-{version}.tgz"
```

Additionally, the `alias` and `main` fields can be used to specify a different name for npm and the main JavaScript file, respectively:
```json
{
  "packages": {
    "reveal.js": "5.1.0",
    "reveal_plugins": {
      "external": {
        "plugin1-name": {
          "version": "0.0.0",
          "url": "https://path/to/url.tar.gz"
        },
        "plugin2-name": {
          "version": "1.0.4",
          "alias": "npm-plugin-name",
          "main": "main-file",
          "export": "plugTwo"
        }
      }
    }
  }, // other config options
}
```

- `alias`: Specifies the npm package name if it differs from the plugin name.
- `main`: Specifies the main JavaScript file name if it differs from the plugin name. The `.js` extension is optional.
- `export`: Specifies the name of the object created when importing the plugin if different from the plugin name.
- `noscript`: When set to `true`, prevents the plugin script tag from being generated in the HTML template.
- `omit`: When set to `true`, prevents the plugin from being listed in the Reveal.js plugin list in the HTML template.

RevealPack will automatically cache downloaded plugins in the `directories.source.root` directory in a sub-folder `cached`. These plugins will be copied, unmodified, upon [`build`](build.md) and a reference will be generated with the expected relative reference:

```html
<script src="./src/plugin/{alias}/{main}.js"></script>
<script>
  Reveal.initialize({
    ... // other configurations
    plugins: ["{export || name}"]
  });
</script>

```
Where `{alias}` and `{main}` are placeholders for the alias and main file name, respectively. If `alias` is not provided, `{plugin}` will be used as the placeholder for the plugin name. Thus, the plugin shall have, e.g., `plugin2-name.js` or `main-file.js` in the unpacked directory. This is a common convention at the time of writing for Reveal.js plugins. Note that the directory unpacked from the url, or npm repo, download will be automatically named `f"{plugin}-{version}"` during the download and setup process. The optional `export` parameter specifies to construct the plugin name for Reveal as the value of `export`, otherwise it will use the plugin name. In our example above, we would get: `plugins: ['plugTwo']` in our reveal template file. If not provided, the assumed exported name is the capitalized version of the plugin name, e.g., `"Plugin2-name"` as above.

If needed, the possible extensions for the `url` may be one of: `.zip`, `.tar.gz`, or `.js`. In the `.js` case, the JavaScript file will be downloaded to the cached directory under `f"{plugin}-{version}/{plugin}.js"`.

Here is an example of how to use the `alias` and `main` fields:
```json
{
  "packages": {
    "reveal.js": "5.1.0",
    "reveal_plugins": {
      "external": {
        "vizzy": {
          "version": "1.0.3",
          "alias": "vizzy-custom",
          "main": "vizzy-main"
        }
      }
    }
  }
}
```
In this example, the plugin will be referenced in the HTML as:
```html
<script src="./src/plugin/vizzy-custom/vizzy-main.js"></script>
```

### Enhanced MathJax Processing

RevealPack includes enhanced MathJax processing that supports flexible version specification. When using the `math` built-in plugin, you can specify MathJax configurations using the `mathjax#` pattern where `#` can be empty, 2, 3, or 4.

#### Configuration Examples

```json
{
  "packages": {
    "reveal_plugins": {
      "built_in": ["math"],
      "plugin_configurations": {
        "mathjax": {
          "mathjax": "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
        },
        "mathjax2": {
          "mathjax": "https://cdn.jsdelivr.net/npm/mathjax@2.7.9/MathJax.js"
        },
        "mathjax3": {
          "mathjax": "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
        },
        "mathjax4": {
          "mathjax": "https://cdn.jsdelivr.net/npm/mathjax@4.0.0-beta.6/tex-mml-chtml.js"
        }
      }
    }
  }
}
```

The system will automatically detect the `mathjax#` pattern and generate the appropriate plugin name:
- `mathjax` → `RevealMath`
- `mathjax2` → `RevealMath.MathJax2`
- `mathjax3` → `RevealMath.MathJax3`
- `mathjax4` → `RevealMath.MathJax4`

This allows for flexible MathJax version configuration without strict validation of the version number.


### `custom_scripts`

The `custom_scripts` configuration option allows you to include custom JavaScript files in your Reveal.js presentations. These scripts are specified in the `config.json` file and will be copied to the build directory during the build process. Each script will be inserted into the head of the generated HTML template, ensuring they are included in your presentation.

#### Configuration

In your `config.json` file, add an array under the `custom_scripts` key with the names of your JavaScript files. These scripts should be located in a subdirectory of the project root called `custom_scripts`.

Example `config.json`:

```
{
  "custom_scripts": [
    "custom1.js",
    "custom2.js"
  ]
}
```

#### How It Works

1. **Specify Scripts**: List your custom JavaScript files in the `custom_scripts` array in `config.json`.
2. **File Location**: Ensure that the specified scripts are placed in the `custom_scripts` directory in the project root.
3. **Build Process**: During the build process, these scripts will be copied to the `<build>/<libraries>/custom_scripts/` directory.
4. **Template Insertion**: The build process will insert the appropriate `<script>` tags into the head of the generated HTML template for each custom script.

Example script tags inserted into the HTML template:

```
<script src="./lib/custom_scripts/custom1.js"></script>
<script src="./lib/custom_scripts/custom2.js"></script>
```

By configuring `custom_scripts`, you can easily include custom functionality and extend your Reveal.js presentations with additional JavaScript code.

To see a complete example for the configuration see [Template](template.md)

### Build Settings

The `build_settings` configuration allows you to control how the build process handles code formatting and whitespace preservation.

#### Configuration

```json
{
  "build_settings": {
    "preserve_code_formatting": true,
    "html_indent_size": 2
  }
}
```

#### Options

- **`preserve_code_formatting`** (boolean, default: `true`): When enabled, preserves whitespace and indentation in code blocks (`<pre>` and `<code>` elements) during the build process. This ensures that code examples maintain their proper formatting without requiring HTML entities like `&#9;` for tabs.

- **`html_indent_size`** (integer, default: `2`): Controls the number of spaces used for HTML indentation in the beautified output. This affects the overall HTML structure while preserving code block formatting.

**Note**: These settings are enabled by default to provide the best user experience for code-heavy presentations. Disable `preserve_code_formatting` only if you have specific formatting requirements that conflict with whitespace preservation.

