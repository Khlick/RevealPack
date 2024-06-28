# RevealPack Documentation

Welcome to the RevealPack documentation. RevealPack is a command-line interface (CLI) tool for managing and building multiple Reveal.js presentations.

## Motivation

RevealPack is more than just a Reveal.js presentation starter; it's a comprehensive framework for creating suites of presentations that share themes and resources, such as a lecture series or a multi-day seminar. RevealPack abstracts much of the slide deck creation process, allowing for complete control over individual slides or groups of slides within each presentation. 

With RevealPack, you can:
- Create slides individually or group multiple slides in one file.
- Share raw HTML or Markdown slides with others.
- Create section title slides or decorate the `section` tag with YAML headers.
- Serve your presentation during development with live updating for smart automatic rebuilds of changed files.

## Commands

- [`init`](init.md): Initialize the directory structure.
- [`setup`](setup.md): Set up the environment.
- [`build`](build.md): Build the presentations.
- [`serve`](serve.md): Serve the presentations locally.
- [`package`](package.md): Package the presentation for distribution.
- `docs`: View the documentation.

## Installation

### Requirements

- Python >3.9, (>=3.12 recommended)

### Install RevealPack from PyPI

To install RevealPack, run:

```bash
pip install revealpack
```

_Note: Use the appropriate method for your setup, e.g., `pip3` or `python -m pip...`._

## Workflow

### Initial Setup

1. **Choose a Project Directory**: Select a directory for your project. It is recommended to create a Python virtual environment in your chosen directory (`root`) and install RevealPack there, rather than using a global environment.

2. **Initialize the Project**: Navigate your terminal or command window to the root directory, activate your Python 3 environment, and use the `revealpack init` command to initialize the directory for your presentations.

```bash
revealpack init
```

3. **Modify Configuration**: Customize the `config.json` file for your project.

4. **Setup Development Environment**: Set up the presentation development environment with the `revealpack setup` command.

```bash
revealpack setup
```

### Presentation Development Workflow

- **Build Presentations**: Use `revealpack build` to compile your presentations.

```bash
revealpack build
```

- **Serve Presentations Locally**: Use `revealpack serve` to start a local server with live reloading for development.

```bash
revealpack serve
```

- **Package Presentations for Distribution**: Use `revealpack package` to package your presentations into a distributable format.

```bash
revealpack package --dest-dir <build_directory> [--root <root_directory>] [--no-build]
```

  - `--dest-dir`: Required. Directory to create the package.
  - `--root`: Optional. Root directory for the package (default is the current working directory).
  - `--no-build`: Optional. Skip the build step (default is to run `revealpack build` before packaging).

For example, to package your presentations without rebuilding, you would run:

```bash
revealpack package --dest-dir path/to/new/package --no-build
```

## Development

For more detailed information on development, see the [Developer's Guide](dev.md).
