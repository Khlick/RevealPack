# Template

This template is designed to be highly customizable using Jinja2 (Liquid) templating, making it ideal for creating dynamic and personalized presentations.

### Key Features:

- **Header Injections**: The template allows for the injection of custom CSS, JavaScript, and raw HTML directly into the `<head>` section. These are specified in the presentation's configuration (`deck.head.styles`, `deck.head.scripts`, `deck.head.raw`), enabling you to include additional resources like fonts, external libraries, or metadata as needed.

- **`.reveal .slides` Section**: The main content area of the presentation, where slides are dynamically generated. 
  - **Title Slide Customization**: If defined (`deck.titlepage`), the title slide is fully customizable, with options for background images, headlines, sub-headers, bylines, and speaker notes. 
  - **Section Titles**: Custom section title slides are supported, with automatic numbering and options for background images, colors, or gradients.

- **Custom Title-Slide Templating**: The title slide is not just a basic header but can be tailored with backgrounds, images, multi-line headlines, sub-headers, bylines, and notes. This flexibility ensures that your presentation starts with a professional, branded slide.

For detailed customization options, refer to the [presentation.md](#) documentation.

This template provides a robust foundation for building polished presentations with Reveal.js, offering extensive customization through Jinja2 templating.

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
    "build": "build",
    "package": "dist",
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
        "splash": {
          "version": "1.0.1",
          "alias": "reveal-splash",
          "main": "reveal-splash"
        },
        "vizzy": {
          "version": "1.1.12",
          "alias": "vizzy-reveal",
          "main": "vizzy"
        }
      },
      "plugin_configurations": {
        "mathjax3": {
          "mathjax": "https://cdn.jsdelivr.net/npm/mathjax@4.0.0-beta.7/tex-mml-chtml.js",
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
        },
        "splash": {
          "image": "img/yourSplash.svg",
          "text": "Loading The Presentation..."
        }
      }
    }
  },
  "theme": "custom_theme/theme.css",
  "reveal_template": "reveal_template.html",
  "toc_template": "toc_template.html",
  "logging": "warning",
  "highlight_theme": "custom_theme/hybrid.css",
  "custom_scripts": [],
  "force_plugin_download": true,
  "reveal_configurations": {
    "controls": true,
    "progress": true,
    "slideNumber": true,
    "history": true,
    "center": true,
    "transition": "slide",
    "hash": true
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
  <link rel="stylesheet" href="./src/theme/theme.css" id="theme">
  <!-- highlight.js theme -->
  <link rel="stylesheet" href="./src/theme/hybrid.css" id="highlight-theme">
  <!-- Custom CSS -->

  <!-- Custom Scripts -->

  <!-- Print PDF and Show logic -->
  <script>
    const params = window.location.search.replace('?', '').split('+');
    const hasPrintPDF = params.includes('print-pdf');
    const hasShow = params.includes('show');

    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.type = 'text/css';
    link.href = hasPrintPDF ? './src/css/print/pdf.css' : './src/css/print/paper.css';
    document.head.appendChild(link);

    if (hasPrintPDF && hasShow) {
      const style = document.createElement('style');
      style.innerHTML = `
        html.print-pdf .reveal .slides .pdf-page section .print-invisible,
        html.reveal-print .reveal .slides .pdf-page section .print-invisible {
          visibility: visible !important;
          display: block !important;
        }
      `;
      document.head.appendChild(style);
    }
  </script>
  <!-- Deck CSS Injections -->
  {% if deck.head and deck.head.styles %}
  {% for style in deck.head.styles %}
  <link rel="stylesheet" href="./lib/{{ style }}">
  {% endfor %}
  {% endif %}
  <!-- Deck Script Injections -->
  {% if deck.head and deck.head.scripts %}
  {% for script in deck.head.scripts %}
  <script src="./lib/{{ script }}"></script>
  {% endfor %}
  {% endif %}
  <!-- Deck Raw Injections -->
  {% if deck.head and deck.head.raw %}
  {% for entry in deck.head.raw %}
  {{ entry }}

  {% endfor %}
  {% endif %}
</head>

<body>
  <div class="reveal">
    <div class="slides">
      {% if deck.titlepage %}
      <section id="deck-title-slide" {%- if deck.titlepage.background -%}{%- for i, v in deck.titlepage.background.items() -%} data-background-{{ i }}="{{ v }}" {%- endfor -%}{%- endif -%}>
        <div class="title-slide{%- if deck.titlepage.background %} background{%- endif -%}">
          {% if deck.titlepage.image %}
          <div class="image" style="background-image: url({{ deck.titlepage.image }});"></div>
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
      <section id="section-title-{{ section_count.n }}" {% if slide.sectiontitle.image -%} data-background-image="{{ slide.sectiontitle.image.url }}" {% for key, value in slide.sectiontitle.image.items() if key != 'url' -%} data-background-{{ key }}="{{ value }}" {% endfor -%} {%- elif slide.sectiontitle.color -%} data-background-color="{{ slide.sectiontitle.color }}" {%- elif slide.sectiontitle.gradient -%} data-background-gradient="{{ slide.sectiontitle.gradient }}" {%- endif -%}>
        <div class="grid-wrapper">
          <div class="section-title-content" id="section-content-{{ section_count.n }}">
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
  <script src="./src/plugin/reveal-splash/reveal-splash.js"></script>
  <script src="./src/plugin/vizzy-reveal/vizzy.js"></script>
  <script>
    Reveal.initialize({
      controls: true,
      progress: true,
      slideNumber: true,
      history: true,
      center: true,
      transition: "slide",
      hash: true
      plugins: [RevealNotes, RevealHighlight, RevealMath, Splash, Vizzy],
      mathjax3: {
        mathjax: "https://cdn.jsdelivr.net/npm/mathjax@4.0.0-beta.7/tex-mml-chtml.js",
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

## Print Functionality

The RevealPack template includes enhanced print functionality that extends Reveal.js's built-in print capabilities.

### Print Modes

The template supports two print modes through URL parameters:

- **Normal Print**: `?print-pdf` - Standard Reveal.js print mode
- **Show Hidden Elements**: `?print-pdf+show` - Shows elements with the `print-invisible` class

### Print-Invisible Class

The template includes CSS support for the `print-invisible` class, which hides elements during normal print mode:

```css
.print-invisible {
  visibility: hidden !important;
}
```

When using `?print-pdf+show`, these elements become visible in the printed output through additional CSS rules:

```css
html.print-pdf .reveal .slides .pdf-page section .print-invisible,
html.reveal-print .reveal .slides .pdf-page section .print-invisible {
  visibility: visible !important;
  display: block !important;
}
```

### Usage Examples

**Hide speaker notes in normal print:**
```html
<aside class="notes print-invisible">
  <p>Speaker notes that are hidden in print by default</p>
</aside>
```

**Hide interactive elements:**
```html
<div class="print-invisible">
  <button onclick="showAnswer()">Click to reveal answer</button>
</div>
```

**Hide supplementary content:**
```html
<div class="print-invisible">
  <p>Additional information for presentation only</p>
</div>
```

### JavaScript Implementation

The print functionality is implemented through JavaScript that:

1. Parses URL parameters to detect print mode and show flag
2. Dynamically loads appropriate CSS files (pdf.css or paper.css)
3. Injects additional CSS rules when `+show` is present
4. Ensures proper visibility of print-invisible elements in show mode
```