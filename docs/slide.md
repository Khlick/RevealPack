# Slide Options

Slides may exist as standalone html files with YAML header information, or as groups of slides, i.e., a single html may contain multiple `<section></section>` elements. The YAML front matter may contain section title information[^1] or provide attributes to the opening `<section>` tag for the first slide in the document.


## Specific Configurations

### `sectiontitle`

The `sectiontitle` field is used to define a section title slide. It includes various subfields to customize the appearance and content of the section title.

#### Fields

| Field       | Type        | Description                                                                                           |
|-------------|-------------|-------------------------------------------------------------------------------------------------------|
| `headline`  | Array       | An array of strings representing the headlines of the section title. The first element is rendered as an `<h2>`, and subsequent elements as `<h3>`. |
| `image`     | Object      | An optional object to specify a background image for the section title. Must contain a `url` field for the image source and can include additional styling properties. |
| `color`     | String      | An optional field to set the background color of the section title. This is used if `image` is not provided. |
| `gradient`  | String      | An optional field to set the background gradient of the section title. This is used if `image` and `color` are not provided. |

### Attributes

Any entries in the slide YAML header that do not match "sectiontitle" will be converted directly to HTML attributes and inserted into the opening <section> tag of the first slide in the document. This includes data attributes, CSS classes, IDs, and more.

## Example

### Single Slide

A single slide HTML file does not require explicit `<section>` tags, as they are handled by the template.

```html
---
---
<div class="grid-wrapper">
  <div class="header">
    <h2>Today's Objectives</h2>
  </div>
  <div class="content">
    <div class="grid-generic full-width left-justify big" style="grid-template-columns: 1fr; grid-auto-rows: auto; row-gap: 5vmin;">
      <div class="border-bottom fragment" data-fragment-index="1">
        <p><i class="target"></i> Recap Repeated-Measures ANOVA</p>
      </div>
      <div class="border-bottom fragment" data-fragment-index="2">
        <p><i class="target"></i> Two-Way ANOVA Introduction</p>
      </div>
    </div>
  </div>
</div>
<aside class="notes">
  <p>Let's recap some of the concepts of ANOVA.</p>
</aside>
```

### Multiple Slides with Section Title

When multiple slides and a section title exist in a single file, the section title `<section>` tag must be explicitly closed before opening the next slide's `<section>` tag.

```html
---
sectiontitle:
  headline:
    - "Factor Analysis"
    - "Two-Way ANOVA"
  image:
    url: "lib/img/multigroup_5.png"
---

<style>
  #section-content-2.section-title-content {
    background-color: rgba(240,240,240,0.7) !important;
    border-radius: 2rem !important;
    box-shadow: 0 0 2rem 2rem rgba(240,240,240,0.7) !important;
  }
</style>
</section>
<!-- Slide 2 -->
<section>
  <div>Slide 2 content here.</div>
</section>
<!-- Slide 3 -->
<section>
  <div>Slide 3 content here.</div>
<!-- no closing section tag -->
```

Which renders[^2] in the presentation as:
```html
<section id="section-title-2" data-background-image="lib/img/multigroup_5.png">
    <div class="grid-wrapper">
        <div class="section-title-content" id="section-content-2">
            <div class="section-number">
                <span class="large-number">2</span>
            </div>
            <div class="headlines">
                <h2 class="r-fit-text">Factor Analysis</h2>
                <h3>Two-Way ANOVA</h3>
            </div>
        </div>
    </div>
    <style>
        #section-content-2.section-title-content {
            background-color: rgba(240,240,240,0.7) !important;
            border-radius: 2rem !important;
            box-shadow: 0 0 2rem 2rem rgba(240,240,240,0.7) !important;
        }
    </style>
</section>
<!-- Slide 2 -->
<section>
    <div>Slide 2 content here.</div>
</section>
<!-- Slide 3 -->
<section>
    <div>Slide 3 content here.</div>
<!-- no closing section tag -->
 </section> <!-- This tag automatically inserted by revealpack -->
```

### Vertical Slide Stack

To create a vertical slide stack, ensure each slide is wrapped in `<section>` tags, and the YAML front matter must be empty.

```html
---
---
<section>
  <h2>Top slide in vertical stack.</h2>
</section>
<section>
  <h2>Second slide in vertical stack.</h2>
</section>
<section>
  <h2>Third slide in vertical stack.</h2>
</section>
```
Which renders in the presentation as:
```html
<section><!-- This tag automatically inserted by revealpack -->
  <section>
    <h2>Top slide in vertical stack.</h2>
  </section>
  <section>
    <h2>Second slide in vertical stack.</h2>
  </section>
  <section>
    <h2>Third slide in vertical stack.</h2>
  </section>
</section><!-- This tag automatically inserted by revealpack -->
 
```

### Attributes

The YAML header can add custom attributes to the opening `<section>` tag. These attributes can include data attributes, IDs, classes, and more. Any YAML entries that do not match "sectiontitle" will be converted directly to HTML attributes.

```html
---
data-background-color: "red"
id: "custom-id"
class: "custom-class"
---
<h2>Add Attributes to Slides</h2>
<div style="width:70vw;"><p>Slide content with custom attributes.</p></div>
```

Which renders in the final presentation as:
```html
<section data-background-color="red" id="custom-id" class="custom-class">
  <h2>Add Attributes to Slides</h2>
  <div style="width:70vw;"><p>Slide content with custom attributes.</p></div>
</section><!-- This tag automatically inserted by revealpack -->
```

By using these YAML options, you can create flexible and well-structured presentations with custom section titles and attributes.


[^1]: If a section title and subsequent slides exist in a single file, the section title `<section>` tag (hidden) must be explicitly closed before opening the next slide's `<section>` tag (see [`Getting Started`](example.md)).
[^2]: To ensure the custom style block is parsed to the correct sectiontitle, make sure you manually select the correct index of section titles. In this example, "Factor Analysis" was the second section title slide in the presentation, hence the specific css selector: `#section-content-2.section-title-content`. Note that RevealPack tracks each section title and increments, so the next section title YAML will have the section tag with `id="section-title-3"` and so on. Likewise, the main text container will have `class="section-title-content"` and `id="section-content-3"`, and so on for future section title slides.