# Presentation Options

Within your working decks directory
(`<project root>/config.directories.source.root/config.directories.source.presentation_root`),
each presentation shall reside in a subdirectory with an indexable name, e.g.,
Lecture 01, as they appear alphabetically in the table of contents (see
[`build`](build.md)). The presentation directory may contain html files containing
slides (`section`s) its presentation and a `presentation.json` containing
configurations for the whole presentation.

## `presentation.json`

The `presentation.json` file is used to configure the properties and behavior of a
presentation deck. This JSON file may contain several fields that control the title
page, slides, footer, and head elements like custom scripts and styles. Below is an
overview of the possible fields and how they are used:

### Fields

| Field       | Sub-Field    | Description                                                                              | Options                                               |
| ----------- | ------------ | ---------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `titlepage` |              | Contains metadata and styling for the title page of the presentation.                    |                                                       |
|             | `headline`   | An array of strings representing the main headlines for the title page.                  | Array of strings                                      |
|             | `by`         | The author(s) of the presentation.                                                       | Array of strings                                      |
|             | `byinfo`     | Additional information about the author(s) such as date, affiliation, etc.               | Array of strings                                      |
|             | `background` | Styling for the title page background. Can include fields such as `image` (URL), `size`. | Object with `image`, `size`, etc.                     |
|             | `image`      | There is a slide-contents sized frame to set an image in.                                | String (e.g. `lib/img/lecture1.png`)                  |
| `footer`    |              | Contains footer information.                                                             |                                                       |
|             | `left`       | Content for the left part of the footer.                                                 | String                                                |
|             | `middle`     | Content for the middle part of the footer.                                               | String                                                |
|             | `right`      | Content for the right part of the footer.                                                | String                                                |
| `slides`    |              | An array of HTML filenames that represent the slides in the presentation.                | Array of strings                                      |
| `head`      |              | Contains optional head elements such as custom scripts and styles.                       |                                                       |
|             | `scripts`    | An array of JavaScript filenames to be included in the head of the HTML.                 | Array of strings (file paths relative to `libraries`) |
|             | `styles`     | An array of CSS filenames to be included in the head of the HTML.                        | Array of strings (file paths relative to `libraries`) |
|             | `raw`        | An array of raw HTML strings to be injected directly into the head of the HTML.          | Array of strings                                      |

## Specific Configurations

### `titlepage`

The `titlepage` field in the `presentation.json` file configures the initial title
slide of the presentation. This field contains several sub-fields that allow for
detailed customization of the title slide. Below are the sub-fields and their
options:

| Sub-Field    | Description                                                                                          | Options                               |
| ------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `headline`   | An array of strings representing the main headline and sub-headline text.                            | Array of strings                      |
| `image`      | The URL of an image to be used as a background for the title slide.                                  | String (URL)                          |
| `background` | An object containing key-value pairs for background properties such as size, position, repeat, etc.  | Object with CSS background properties |
| `by`         | A string or an array of strings representing the author(s) of the presentation.                      | String or array of strings            |
| `byinfo`     | A string or an array of strings for additional author information such as date, affiliation, etc.    | String or array of strings            |
| `notes`      | An array of strings representing notes or additional information to be displayed in the notes panel. | Array of strings                      |

#### `headline`

The `headline` field contains the main title and subtitle of the presentation. It
should be an array of strings. The first string is rendered as a larger title, and
subsequent strings are rendered as subtitles.

**Example:**

```json
"titlepage": {
  "headline": [
    "Analysis of Variance 3",
    "ANOVA Does Even More"
  ]
}
```

Rendered HTML Snippet:

```html
<section id="deck-title-slide">
  <div class="title-slide">
    <div class="headline">
      <h2 class="r-fit-text">Analysis of Variance 3</h2>
      <h3>ANOVA Does Even More</h3>
    </div>
    <div class="sub-header"></div>
    <div class="byline"></div>
  </div>
</section>
```

#### `image`

The `image` field sets a centered image for the title slide. It is a string
containing the URL of the image. The image will be placed in a templated `div`
(`class="image"`) which is centered on the slide based on
[`revealpack.css`](styles.md) rules. _Note: this is a distinction from
`background.image` below, which will be handled by the Reveal.js backgrounds
mechanism._

**Example:**

```json
"titlepage": {
  "image": "lib/img/power_1.png"
}
```

Rendered HTML Snippet:

```html
<section id="deck-title-slide">
  <div class="title-slide">
    <div class="image" style="background-image: url(lib/img/power_1.png);"></div>
    <div class="headline"></div>
    <div class="sub-header"></div>
    <div class="byline"></div>
  </div>
</section>
```

#### `background`

The `background` field is an object that defines various background properties such
as size, position, repeat, etc. These properties are applied to the title slide's
background. These attributes are added to the `section` tag as
`data-background-<attr>` and are formatted to be used with
[Reveal.js background properties](https://revealjs.com/backgrounds). Thus, a background could contain an image, a gradient, a solid color, etc..
_Note: this is a
distinction from `image` above, which will be placed in a `div` element styled by
[`revealpack.css`](styles.md) and constrained to the slide's viewable area._

**Example:**

```json
"titlepage": {
  "background": {
    "image": "lib/img/power_1.png",
    "size": "cover",
    "position": "center",
    "repeat": "no-repeat",
    "opacity": 0.5
  }
}
```

Rendered HTML Snippet:

```html
<section
  id="deck-title-slide"
  data-background-image="lib/img/power_1.png"
  data-background-size="cover"
  data-background-position="center"
  data-background-repeat="no-repeat"
  data-background-opacity="0.5"
>
  ...
</section>
```

#### `by`

The `by` field contains the author(s) of the presentation. It can be a string or an
array of strings.

**Example:**

```json
"titlepage": {
  "by": "Khris Griffis, Ph.D."
}
```

Rendered HTML Snippet:

```html
<section id="deck-title-slide">
  <div class="title-slide">
    <div class="headline"></div>
    <div class="sub-header">
      <p class="by">Khris Griffis, Ph.D.</p>
    </div>
    <div class="byline"></div>
  </div>
</section>
```

#### `byinfo`

The `byinfo` field provides additional information about the author(s) such as date,
affiliation, etc. It can be a string or an array of strings.

**Example:**

```json
"titlepage": {
  "byinfo": [
    "April 10, 2024",
    "CSULA: ME3040 Spring 2024"
  ]
}
```

Rendered HTML Snippet:

```html
<div class="byline">
  <p class="byinfo">April 10, 2024</p>
  <p class="byinfo">CSULA: ME3040 Spring 2024</p>
</div>
```

#### `notes`

The `notes` field contains additional information or notes for the title slide. These
notes are displayed in the speaker notes panel.

**Example:**

```json
"titlepage": {
  "notes": [
    "Let's recap some of the concepts of ANOVA.",
    "Prepare for interactive questions."
  ]
}
```

Rendered HTML Snippet:

```html
<section id="deck-title-slide">
  <div class="title-slide">...</div>
  <aside class="notes">
    <p>Let's recap some of the concepts of ANOVA.</p>
    <p>Prepare for interactive questions.</p>
  </aside>
</section>
```

### `footer`

The presentation has a static position for the footer information organized by left,
middle, and right horizontal alignments. This is a good place to put common elements
for every slide, such as branding, copywrite, etc..

### `head`

The `head` object in the `presentation.json` file allows for the inclusion of custom
stylesheets, scripts, and raw HTML within the `<head>` section of the generated HTML.
This provides flexibility for advanced customization of your presentations.

#### Fields

| Field     | Type  | Description                                                                                                                                                   |
| --------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `styles`  | Array | An array of stylesheet file paths to be included in the `<head>` section. These paths are relative to the `libraries` directory specified in the config.json. |
| `scripts` | Array | An array of script file paths to be included in the `<head>` section. These paths are relative to the `libraries` directory specified in the config.json.     |
| `raw`     | Array | An array of raw HTML strings to be injected directly into the `<head>` section. Each entry is rendered on its own line.                                       |

### Detailed Descriptions

#### `styles`

The `styles` field allows you to specify additional CSS files that should be included
in the `<head>` section of your HTML. Each file path is relative to the `libraries`
directory defined in your `config.json`. These stylesheets will be added after the
default stylesheets, allowing you to override or extend the default styles.

#### `scripts`

The `scripts` field allows you to specify additional JavaScript files that should be
included in the `<head>` section of your HTML. Each file path is relative to the
`libraries` directory defined in your `config.json`. These scripts will be added
after the default scripts, enabling you to add custom functionality or modify
existing behavior.

#### `raw`

The `raw` field allows you to inject raw HTML strings directly into the `<head>`
section of your HTML. This is useful for adding meta tags, inline styles, or other
HTML elements that are not covered by the `styles` and `scripts` fields. Each entry
in the `raw` array will be rendered on its own line in the `<head>` section.

## Examples

#### Example 1: Basic Presentation

`Session 1/presentation.json`:

```json
{
  "titlepage": {
    "headline": ["Introduction to Machine Learning", "Basics and Beyond"],
    "by": ["Jane Doe"],
    "byinfo": ["January 1, 2024", "Machine Learning Conference"],
    "background": {
      "image": "lib/img/ml_background.png",
      "size": "cover"
    }
  },
  "footer": {
    "left": "Session 1",
    "middle": "",
    "right": "Jane Doe ©2024"
  },
  "slides": ["intro.html", "overview.html", "details.html"]
}
```

**Rendered HTML Snippet:**

The first slide in the presentation is populated by the presentation.json `titlepage`
object.

`Session 1.html`

```html
...
<body>
  <div class="reveal">
    <div class="slides">
      <section
        id="deck-title-slide"
        data-background-image="lib/img/ml_background.png"
        data-background-size="cover"
      >
        <div class="title-slide">
          <div class="headline">
            <h2 class="r-fit-text">Introduction to Machine Learning</h2>
            <h3>Basics and Beyond</h3>
          </div>
          <div class="sub-header">
            <p class="by">Jane Doe</p>
          </div>
          <div class="byline">
            <p class="byinfo">January 1, 2024</p>
            <p class="byinfo">Machine Learning Conference</p>
          </div>
        </div>
      </section>
      <section>
        <!-- Contents of intro.html -->
      </section>
      <section>
        <!-- Contents of overview.html -->
      </section>
      <section>
        <!-- Contents of details.html -->
      </section>
      ...
    </div>
    <!-- slides -->
    <footer class="main-footer">
      <span>Session 1</span>
      <span style="text-align:center;"></span>
      <span style="text-align:right;">Jane Doe ©2024</span>
    </footer>
  </div>
  <!-- reveal -->
  <script src="./src/reveal.js"></script>
  <!-- Reveal.js Plugins and Initializations -->
</body>
...
```

#### Example 2: Presentation with Custom Scripts and Styles

We can inject custom scripts, stylesheets, and raw html directly into the head of a
presentation by supplying the `head` object in the `presentation.json` file.

```json
{
  "titlepage": {
    "headline": ["Advanced Data Science", "Techniques and Tools"],
    "by": ["John Smith"],
    "byinfo": ["February 15, 2024", "Data Science Summit"],
    "background": {
      "image": "lib/img/data_science.png",
      "size": "cover"
    }
  },
  "footer": {
    "left": "Session 2",
    "middle": "",
    "right": "John Smith ©2024"
  },
  "slides": ["intro.html", "techniques.html", "tools.html"],
  "head": {
    "scripts": ["lib/js/custom_script.js"],
    "styles": ["lib/css/custom_style.css"],
    "raw": ["<meta name='custom-meta' content='example'>"]
  }
}
```

**Rendered HTML Snippet:**

```html
<head>
  <!-- Reveal.js and Theme Configs -->
  <!--  -->
  <!-- Custom Deck Styles -->
  <link rel="stylesheet" href="./lib/css/custom_style.css" />
  <!-- Custom Deck Scripts -->
  <script src="./lib/js/custom_script.js"></script>
  <!-- Custom Deck Raw HTML -->
  <meta name="custom-meta" content="example" />
</head>
<body>
  ...
</body>
```
