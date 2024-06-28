# RevealPack Styles

The RevealPack template presentation comes with style class definitions available to the user and used by the template.

Note, the CSS selector specificity of the below styles is at the level of `.reveal .<class>`. To override or modify any of the styles below, the user may supply their own css (see [Presentation Options](presentation.md) or [RevealPack Configuration](config.md)) with these class name defined with a selector specificity of `.reveal .slides .<class>` to gain precedence (see <a href="https://www.w3schools.com/css/css_specificity.asp" target="_blank">CSS Specificity</a>).

## Exposed Styles

The sections below describe the classes available to the user for understanding some of the templated layout, but also for their own use.

### `.title-slide`

- Sets the grid layout for title slides with 4 rows and 5 columns.
- Uses the `fill-view` mixin to scale the content to fit the view.

#### `.image`

- Spans the entire grid.
- Background image settings include no-repeat, center positioning, and contain size.
- Positioned at `z-index: 1` to stay behind other elements.

#### `.headline`

- Positioned in the top right, spanning 2 columns.
- Uses the `fill-view` mixin to scale the content appropriately.
- Contains a bold `h2` element.
- Positioned at `z-index: 3` to stay in front of the background image.

#### `.sub-header`

- Positioned in the middle right, spanning 2 columns.
- Contains paragraphs with the class `.by`, which have specific font and styling.
- Positioned at `z-index: 3` to stay in front of the background image.

#### `.byline`

- Positioned in the bottom right, spanning 2 columns.
- Contains paragraphs with the class `.byinfo`, which have specific font and styling.
- Positioned at `z-index: 3` to stay in front of the background image.

#### `.background`

- Covers a partial area of the grid, spanning 2 columns.
- Includes gradient background and border-radius styling.
- Positioned at `z-index: 2` to stay behind the headline, sub-header, and byline.
- Includes a margin adjustment for alignment.

### `.grid-wrapper`

The `.grid-wrapper` class defines a responsive grid layout for the slide content, with specific areas for the header, content, and footer. The `fill-view` mixin scales the element to fit the view. It includes three rows (header, content, footer) and three columns (foot-left, foot-center, foot-right). While this class is primarily used for section title slides (see [Slide Options](slide.md)), it may be useful should the user wish to employ a grid layout system for slides (see [Using RevealPack](example.md)).

#### Properties:
- **Margin & Padding**: Resets to zero for a clean layout.
- **Box-sizing**: Set to `border-box` for consistent sizing.
- **Display**: Uses CSS Grid to create a structured layout.
- **Grid Template Areas**: Defines named grid areas for easier placement of child elements.
- **Grid Template Rows**: Allocates space for header, content, and footer with auto, 1fr, and min-content sizes respectively.
- **Grid Template Columns**: Three equal columns.

#### Nested Elements:
- **`.header`, `h2`**: Positioned in the header area, centered both vertically and horizontally.
- **`.content`**: Positioned in the content area, uses flexbox for child alignment.
- **`.foot-left`, `.foot-center`, `.foot-right`**: Positioned in the footer areas, with respective text alignment and smaller font size.

#### `.section-title-content`:
- **Grid Layout**: Specific to section titles, with areas for section number and headlines.
- **Child Elements**:
  - **`.section-number`**: Displays the section number, styled with a large font.
  - **`.headlines`**: Contains the headlines, styled with different font families and colors.

### No Margin

`.no-margin`: Removes margin and padding from an element.

### Generic Styles

- `.strong`: Bold text
- `.em`: Italic text
- `.u`: Underlined text
- `.strike`: Strikethrough text
- `.tt`: Monospaced font
- `.sf`: Sans-serif font
- `.full-width`: Full width element
- `.q3-width`: 75% width element
- `.half-width`: 50% width element
- `.q1-width`: 25% width element
- `.box-width`: 80% width element
- `.center-justify`: Center-aligned text
- `.left-justify`: Left-aligned text
- `.right-justify`: Right-aligned text
- `.just-justify`: Justified text

### No Hang

`.no-hang`: Prevents hanging margins and padding for direct children elements.

### PDF Page Adjustments

`.pdf-page`: Adjusts the styles for PDF page output to ensure proper formatting.

## Emojis

### Icon for Any Unicode Character Emoji

`i[role="emoji"]`: Applies styles for any Unicode character emoji using the defined emoji font stack.

### Build Icon for Most Used Emoji List

`i`: Styles the most used emojis list with predefined emoji classes.

### Build `<li>` Emojis

`li.emoji-name`: Applies styles for list items containing emojis, ensuring proper positioning and font size.

### Build `<span>` for Any Emoji

`span.emoji`: Applies styles for span elements containing emojis, ensuring proper display and alignment.

### Predefined Emoji Classes


| Emoji Name       | Class Name         | Rendered Emoji    |
|------------------|--------------------|-------------------|
| Angry            | `.angry`           | 😡                |
| Angry Face       | `.angry_face`      | 🤬                |
| Arrow Right      | `.arrowr`          | →                 |
| Arrow Left       | `.arrorl`          | ←                 |
| Beaker           | `.beaker`          | 🧪                |
| Brain            | `.brain`           | 🧠                |
| Calculator       | `.calculator`      | 🖩                |
| Calendar         | `.calendar`        | 🗓️                |
| Chart            | `.chart`           | 📈                |
| Check            | `.check`           | ✔️                |
| Clock            | `.clock`           | 🕗                |
| Construction     | `.construction`    | 🚧                |
| Cool             | `.cool`            | 😎                |
| Crying           | `.crying`          | 😭                |
| DNA              | `.dna`             | 🧬                |
| Double Exclamation | `.double_exclamation` | ‼️          |
| Exclamation      | `.exclamation`     | ❗                |
| Exclamation Question | `.exclamation_question` | ⁉️      |
| Fire             | `.fire`            | 🔥                |
| Floppy Disk      | `.floppy_disk`     | 💾                |
| Gem Stone        | `.gem_stone`       | 💎                |
| Goggles          | `.goggles`         | 🥽                |
| Happy            | `.happy`           | 🙂                |
| Key              | `.key`             | 🗝️                |
| Lightbulb        | `.lightbulb`       | 💡                |
| Lightning        | `.lightning`       | ⚡                |
| Locked           | `.locked`          | 🔒                |
| Loudspeaker      | `.loudspeaker`     | 📢                |
| Medal            | `.medal`           | 🥇                |
| Memo             | `.memo`            | 📝                |
| Microscope       | `.microscope`      | 🔬                |
| Mirror           | `.mirror`          | 🪞                |
| No Entry         | `.no_entry`        | 🚫                |
| No Entry Sign    | `.no-entry`        | ⛔                |
| Party Popper     | `.party_popper`    | 🎉                |
| Pin              | `.pin`             | 📌                |
| Question         | `.question`        | ❓                |
| Report           | `.report`          | 📝                |
| Ribbon           | `.ribbon`          | 🎗️                |
| Sad              | `.sad`             | 😞                |
| Scream           | `.scream`          | 😱                |
| Sigh             | `.sigh`            | 😔                |
| Skull and Crossbones | `.skull_and_crossbones` | ☠️       |
| Smiley           | `.smiley`          | 😄                |
| Speech Balloon   | `.speech_balloon`  | 🗨️                |
| Star             | `.star`            | 🌟                |
| Star Struck      | `.star-struck`     | 🤩                |
| Stop Sign        | `.stop_sign`       | 🛑                |
| Target           | `.target`          | 🎯                |
| Test Tube        | `.test_tube`       | 🧪                |
| Thought Balloon  | `.thought_balloon` | 💭                |
| Unlocked         | `.unlocked`        | 🔓                |
| Warning          | `.warning`         | 🚨                |

##### Named Emoji Usage


```html
<i class="angry"></i>
```


#### Generic Emoji Role


```html
<i role="emoji" data-emoji="\1F525"></i>
```
Which renders:

 🔥

#### Span Emoji


```html
<span class="emoji">&#x1f525;</span>
```
Which renders:
 🔥
