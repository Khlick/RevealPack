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

## Example `config.json`

Here is an example of what your `config.json` might look like:

```json
{
  "info": {
    "project_title": "My Reveal.js Lectures",
    "short_title": "revealLectures",
    "version": "1.0.0",
    "authors": ["Your Name"]
  },
  "directories": {
    "build": "dist",
    "source": {
      "root": "source",
      "presentation_root": "decks",
      "libraries": "lib"
    }
  },
  "packages": {
    "reveal.js": "5.1.0",
    "reveal_plugins": {
      "built_in": [
        "notes",
        "highlight",
        "math"
      ],
      "external": {
        "vizzy": {
          "version": "1.0.4",
          "alias": "vizzy-reveal",
          "main": "vizzy"
        },
      },
      "plugin_configurations": {
        "mathjax3": {
          "mathjax": "https://cdn.jsdelivr.net/npm/mathjax@4.0.0-beta.6/tex-mml-chtml.js",
          "loader": {
            "load": [
              "[tex]/html"
            ]
          },
          "tex": {
            "packages": {
              "'[+]'": [
                "html"
              ]
            },
            "inlineMath": [
              ["$","$"],
              ["\\(","\\)"]
            ]
          },
          "options": {
            "skipHtmlTags": [
              "script",
              "noscript",
              "style",
              "textarea",
              "pre"
            ]
          }
        },
        "notes": {},
        "highlight": {},
        "vizzy": {
          "autoRunTransitions": true,
          "autoTransitionDelay": 100,
          "devMode": false,
          "onSlideChangedDelay": 0
        }
      }
    }
  },
  "theme": "custom_theme/theme.css",
  "reveal_template": "reveal_template.html",
  "toc_template": "toc_template.html",
  "logging": "detailed",
  "highlight_theme": "custom_theme/hybrid.css",
  "custom_scripts": [],
  "force_plugin_download": true,
  "reveal_configurations": {
    "controls": true,
    "progress": true,
    "slideNumber": true,
    "history": true,
    "center": true,
    "transition": "slide"
  }  
}
```

#### Rendered Reveal (Jinja2) Template

```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>{{deck.title}}</title>
        <link rel="icon" type="image/x-icon" href="lib\favicon.png">
        <link rel="stylesheet" href="./src/css/reset.css">
        <link rel="stylesheet" href="./src/css/reveal.css">
        <link rel="stylesheet" href="./src/theme/drG.css">
        <!-- highlight.js theme -->
        <link rel="stylesheet" href="./src/theme/hybrid.css">
        <!-- Custom Scripts -->

        <!-- Print PDF script -->
        <script>
            var link = document.createElement( 'link' );
            link.rel = 'stylesheet';
            link.type = 'text/css';
            link.href = window.location.search.match( /print-pdf/gi ) ? './src/css/print/pdf.css' : './src/css/print/paper.css';
            document.getElementsByTagName( 'head' )[0].appendChild( link );
        </script>

    </head>
    <body>
        <div class="reveal">
            <div class="slides">
                {% if deck.titlepage %}
                <section id="deck-title-slide" {%- if deck.titlepage.background -%}{%- for i,v in deck.titlepage.background.items() -%} data-background-{{ i }}="{{ v }}"{%- endfor -%}{%- endif -%}>
                    <div class="title-slide">
                    {% if deck.titlepage.image %}
                        <div class="image" style="background-image: url({{ deck.titlepage.image }});">
                        </div>
                    {% endif %}
                    <div class="headline">
                        {% if deck.titlepage.headline %}
                        {% for line in deck.titlepage.headline %}
                        {% if loop.first %}
                        <h2 class="r-fit-text">{{ line|title }}</h2>
                        {% else %}
                        <h3>{{ line|title }}</h3>
                        {% endif %}
                        {% endfor %}
                        {% endif %}
                    </div>
                    <div class="sub-header">
                        {% if deck.titlepage.by %}
                        {% for by in deck.titlepage.by %}
                        <p class="by">{{ by }}</p>
                        {% endfor %}
                        {% endif %}
                    </div>
                    <div class="byline">
                        {% if deck.titlepage.byinfo %}
                        {% for byinfo in deck.titlepage.byinfo %}
                        <p class="byinfo">{{ byinfo }}</p>
                        {% endfor %}
                        {% endif %}
                    </div>
                    <div class="background"></div>
                    </div>
                    {% if deck.titlepage.notes %}
                    <aside class="notes">
                    {% for note in deck.titlepage.notes %}<p>{{ note }}</p>
                    {% endfor %}
                    </aside>
                    {% endif %}
                </section>
                {% endif %}
                {% set section_count = namespace(n = 0) -%}
                {% for slide in deck.slides %}
                {% if slide.sectiontitle %}
                {% set section_count.n = section_count.n + 1 %}
                <section id="section-title-{{ section_count.n }}"{% if slide.sectiontitle.image -%}
                 data-background-image="{{ slide.sectiontitle.image.url }}"{% for key, value in slide.sectiontitle.image.items() if key != 'url' -%} data-background-{{ key }}="{{ value }}"{% endfor -%}
                 {%- elif slide.sectiontitle.color -%}
                 data-background-color="{{ slide.sectiontitle.color }}"
                 {%- elif slide.sectiontitle.gradient -%}
                 data-background-gradient="{{ slide.sectiontitle.gradient }}"
                 {%- endif -%}>
                    <div class="grid-wrapper">
                        <div class="section-title-content"  id="section-content-{{ section_count.n }}">
                        <div class="section-number">
                            <span class="large-number">{{ section_count.n }}</span>
                        </div>
                        <div class="headlines">
                            {% for line in slide.sectiontitle.headline %}
                            {% if loop.first %}
                            <h2 class="r-fit-text">{{ line|title }}</h2>
                            {% else %}
                            <h3>{{ line|title }}</h3>
                            {% endif %}
                            {% endfor %}
                        </div>
                        </div>
                    </div>
                    {{ slide.content }}
                {% else %}
                <section {{ slide.attributes|to_html_attrs|safe }}>
                    {{ slide.content }}
                {% endif %}
                </section>
                {% endfor %}
            </div>
            {% if deck.footer %}
            <footer class="main-footer">
                <span>{{ deck.footer.left if deck.footer.left is defined else '' }}</span>
                <span style="text-align:center;">{{ deck.footer.middle if deck.footer.middle is defined else '' }}</span>
                <span style="text-align:right;">{{ deck.footer.right if deck.footer.right is defined else '' }}</span>
            </footer>
            {% endif %}
        </div>
        <script src="./src/reveal.js"></script>
        <script src="./src/plugin/notes/notes.js"></script>
        <script src="./src/plugin/highlight/highlight.js"></script>
        <script src="./src/plugin/math/math.js"></script>
        <script src="./src/plugin/vizzy/vizzy.js"></script>
        <script src="./src/plugin/reveal.js-menu/reveal.js-menu.js"></script>
        <script>
            Reveal.initialize({
              center: false,
              controls: true,
              controlsBackArrows: "faded",
              controlsLayout: "bottom-right",
              display: "block",
              fragments: true,
              hideAddressBar: true,
              hideCursorTime: 5000,
              keyboard: true,
              mobileViewDistance: 3,
              mouseWheel: false,
              navigationMode: "default",
              overview: true,
              pdfMaxPagesPerSlide: 1,
              pdfSeparateFragments: false,
              preloadIframes: true,
              progress: false,
              showSlideNumber: "print",
              sortFragmentsOnSync: true,
              touch: true,
              transition: "fade",
              transitionSpeed: "default",
              viewDistance: 3,
              width: 1920,
              height: 1080,
              margin: 0.125,
              minScale: 0.1,
              maxScale: 1.25,
              plugins: [ RevealNotes, RevealHighlight, RevealMath, Vizzy ],
              mathjax3: {
                mathjax: "https://cdn.jsdelivr.net/npm/mathjax@4.0.0-beta.6/tex-mml-chtml.js",
                loader: {
                  load: [
                    "[tex]/html",
                  ],
                },
                tex: {
                  packages: {
                    '[+]': [
                      "html",
                    ],
                  },
                  inlineMath: [
                    ["$", "$"],
                    ["\\(", "\\)"],
                  ],
                },
                options: {
                  skipHtmlTags: [
                    "script",
                    "noscript",
                    "style",
                    "textarea",
                    "pre",
                  ],
                },
              },
              notes: {

              },
              highlight: {

              },
              vizzy: {
                autoRunTransitions: true,
                autoTransitionDelay: 100,
                devMode: true,
                onSlideChangedDelay: 0,
              },
            });
        </script>
    </body>
</html>
```