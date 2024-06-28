# `revealpack init`

## Description

The `revealpack init` command initializes the file structure for a new Reveal.js presentation project. It copies a generic `config.json` file and the `assets` directory to the specified destination. Additionally, it creates a `decks` directory for storing individual presentation decks.

## Usage

```sh
revealpack init [OPTIONS]
```

### Options

- `--destination` (optional): The path where `config.json` and `assets` should be copied. If not provided, they will be copied to the current directory.

### Examples

#### Initialize in the Current Directory

To initialize the project structure in the current directory, simply run:

```sh
revealpack init
```

#### Initialize in a Specific Directory

To initialize the project structure in a specific directory, use the `--destination` option:

```sh
revealpack init --destination /path/to/your/project
```

## File Structure

After running the `revealpack init` command, the following structure will be created:

```plaintext
your-project-directory/
├── config.json
└── assets/
    └── ... (revealpack assets)
```

### `config.json`

The `config.json` file is a template configuration file that you can customize to suit your project needs.

Following `init`, modify the properties in `config.json` for your project, adjust theming files as needed then run [`revealpack setup`](setup.md).