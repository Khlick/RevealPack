# `revealpack build`

The `build` command is responsible for converting slide decks located in the specified source directories into individual presentations, including caching plugins and generating the necessary HTML files using Reveal.js. This command processes each subdirectory within the presentation root directory, creating a presentation for each.

#### Options

- `--root <directory>`: Specifies the root directory for the build. Defaults to the current working directory.
- `--clean`: Performs a clean build by removing all contents of the build directory before starting the build process.
- `--decks <file or string>`: Specifies a comma-separated list of deck names or a path to a file containing deck names to be built. If this option is provided, a clean build is automatically performed.

#### Process Overview

1. **Read and Parse Configuration:**
   The `build` command reads the configuration options from the `config.json` file located in the specified root directory.

2. **Perform Clean Build (Optional):**
   If the `--clean` option is used, the build directory is emptied before the build process begins, ensuring no residual files from previous builds.

3. **Determine Decks to Build (Optional):**
   If the `--decks` option is provided, only the specified decks are built. The option accepts either a comma-separated string of deck names or a file path containing deck names.

4. **Copy Libraries:**
   The `build` command copies libraries from the source libraries directory to the build directory, ensuring all necessary assets are included.

5. **Copy Custom Scripts:**
   Custom scripts specified in the `config.json` are copied to the appropriate location in the build directory.

6. **Copy Plugins:**
   Both built-in and external plugins specified in the `config.json` are copied from the cached directory to the build directory.

7. **Compile Theme:**
   If the specified theme is provided as an SCSS/SASS file, it is compiled into a CSS file. If a pre-compiled CSS file is provided, it is used directly.

8. **Copy Reveal.js Files:**
   Relevant Reveal.js files are copied from the cached directory to the build directory, ensuring the necessary JavaScript and CSS files are available for the presentations.

9. **Generate Presentations:**
   The `build` command processes each subdirectory within the presentation root directory, treating each as a separate presentation. It reads any `presentation.json` files for metadata or defaults to parsing HTML files alphabetically.

10. **Generate Table of Contents (TOC):**
    A table of contents (`index.html`) is generated in the build directory, providing links to all built presentations.

#### Expected Behavior

- **Slide Deck Conversion:**
  The command converts each subdirectory within the presentation root directory into a standalone presentation, generating the appropriate HTML files.

- **Plugin Management:**
  The command ensures all specified plugins are downloaded, cached, and copied to the build directory. This includes handling plugins with aliases and main entry points.

- **Theming:**
  The specified theme is compiled (if necessary) and included in the build, along with any related font files.

- **Output:**
  The final output includes a table of contents (`index.html`) and individual presentation HTML files in the build directory.

#### Example Usage

~sh
revealpack build --root /path/to/project --clean --decks "Lecture 01,Lecture 02"
~

This command will read the `config.json` from `/path/to/project`, perform a clean build, process only the specified decks ("Lecture 01" and "Lecture 02"), copy necessary libraries and plugins, compile the theme, and generate the final HTML files in the build directory.

### `config.json` Options

The following `config.json` options are relevant to the `build` command:

- **directories:**
  - **build:** The output directory for the built presentations.
  - **source:**
    - **root:** The root directory for source files.
    - **presentation_root:** The directory containing presentation subdirectories.
    - **libraries:** The directory containing shared libraries.

- **packages:**
  - **reveal.js:** The version of Reveal.js to use.
  - **reveal_plugins:**
    - **built_in:** A list of built-in plugins to include.
    - **external:** A dictionary of external plugins to include, with version, URL, alias, and main entry point.

- **theme:** The path to the theme file, which can be an SCSS/SASS file or a pre-compiled CSS file.

- **custom_scripts:** A list of custom JavaScript scripts to include in the presentations.

- **toc_template:** The path to the template file for the table of contents.

### Note on Presentation Structure

In the `<project root>/config.directories.source.root/config.directories.source.presentation_root` directory, each subdirectory is treated as a separate presentation. Each presentation directory may contain:

- **HTML Files:** Slide contents.
- **presentation.json:** Metadata for the presentation (optional, see [Presentation Options](presentation.md)).

The `presentation.json` may specify custom ordering for slides, title pages, and other metadata.

By following this process, the `build` command ensures that all necessary files are included and properly configured, resulting in fully functional Reveal.js presentations.