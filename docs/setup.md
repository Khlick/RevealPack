# `revealpack setup`

## Prerequisites

**⚠️ Important:** Before running `revealpack setup`, ensure you have Dart Sass CLI installed on your system. RevealPack requires Dart Sass to compile SCSS/SASS theme files, and the build process will fail without it.

**Install Dart Sass:**
- Visit [https://sass-lang.com/install](https://sass-lang.com/install)
- Follow the installation instructions for your operating system
- Verify installation: `sass --version`

**Reveal.js Compatibility:**
- **Tested Version**: Reveal.js 5.2.1
- **Backwards Compatible**: Reveal.js 4.x versions
- **Minimum Version**: Reveal.js 4.0.0

## Description

The `revealpack setup` command sets up the environment for building Reveal.js presentations. It reads the [`config.json`](config.md) file generated in the [`init`](init.md) step, creates necessary directories, downloads and installs Reveal.js packages, checks the theme, and generates the necessary templates used in the next, [`build`](build.md) step.

## Usage

```sh
revealpack setup [OPTIONS]
```

### Options

- `--root` (optional): The target directory for setup. If not provided, the current working directory will be used.

### Examples

#### Setup in the Current Directory

To set up the presentation development environment in the current directory, simply run:

```sh
revealpack setup
```

#### Setup in a Specific Directory

To set up the environment in a specific directory, use the `--root` option. The root directory should contain the `config.json` for your project:

```sh
revealpack setup --root /path/to/your/project
```

## What to Expect

When you run the `revealpack setup` command, the following actions will be performed:

1. **Parse Configuration**:
   - The `config.json` file in the specified root directory (or the current directory if no root is specified) will be read to gather necessary settings for the setup.

1. **Create Directories**:
   - Necessary directories for building and storing the Reveal.js presentations will be created as specified in the `config.json`. This includes directories for source files, libraries, and build outputs:
     - `source` (root directory for source files)
     - `source/lib` (directory for libraries and assets)
     - `source/decks` (directory for individual presentation decks)
     - `dist` (directory for build outputs)
     - `source/cached` (directory for cached packages)

1. **Download and Install Packages**:
   - The specified version of Reveal.js and any additional plugins mentioned in the `config.json` file will be downloaded and installed in the `source/cached` directory. These packages are essential for the functionality and customization of your presentations.

1. **Check Theme**:
   - The theme specified in the `config.json` file will be validated. If the theme is not found, an error will be logged, and the process will stop, prompting you to correct the theme settings.

1. **Generate Templates**:
   - Jinja2 templates for your presentations and table of contents will be generated based on the configurations provided in the `config.json` file. These templates form the structure and style of your presentations.

### After Running `revealpack setup`

Once the setup is complete, your project directory will have the following structure:

```plaintext
your-project-directory/
├── config.json
├── assets/
│   └── ... (revealpack assets)
├── source/
│   ├── lib/
│   │   └── ... (libraries and assets)
│   ├── decks/
│   │   └── ... (individual presentation decks)
│   ├── cached/
│   │   └── ... (cached packages)
│   ├── reveal_template.html
|   └── toc_template.html
└── [dist/] (depending on build directory in config.json)
```

You are now ready to start building and customizing your Reveal.js presentations. The next steps typically involve adding content to your `source/decks` directory and running the `revealpack build` command to compile your presentations. _Note. Changing fields in the [`config.json`](config.md) will modify the names of the subdirectories, but the general structure will remain the same._
