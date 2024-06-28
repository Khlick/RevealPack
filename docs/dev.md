# Developer Guide for RevealPack

This guide provides instructions for developers who want to work with the RevealPack package. It includes steps for setting up the development environment, building the package, and publishing it to PyPI.

## Setup Development Environment

### 1. Clone the Repository

Clone the repository to your local machine:

```sh
git clone https://github.com/Khlick/RevealPack.git
cd RevealPack
```

### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies and avoid conflicts:

```sh
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```

### 3. Install Development Dependencies

Install the required development dependencies:

```sh
pip install -r requirements.txt
pip install build twine
```

---

## Directory Structure for RevealPack

This section provides an overview of the files included in the RevealPack package.

### Project Root File Breakdown

This section provides an overview of the files and directories in the project root.


```
.github/workflows/
docs/
revealpack/
tests/
.gitignore
dev_destroy.py
dev_setup.py
LICENSE
MANIFEST.in
mkdocs.yml
pyproject.toml
README.md
requirements.txt
setup.py
```

### File and Directory Descriptions

#### `.github/workflows/`

- **Purpose**: Contains GitHub Actions workflows for automating tasks such as building and releasing the package.
- **Description**: Workflow files in this directory define the continuous integration and deployment (CI/CD) pipelines for the project.

#### `docs/`

- **Purpose**: Contains the MkDocs documentation files.
- **Description**: This directory includes markdown files and other resources for generating the project's documentation using MkDocs.

#### `revealpack/`

- **Purpose**: Contains the main package code for RevealPack (see below).
- **Description**: This directory includes all the Python modules and packages that make up the RevealPack tool.

#### `tests/`

- **Purpose**: Contains test files for the project.
- **Description**: This directory includes unit tests and other test scripts to ensure the functionality and reliability of the RevealPack package.

#### `.gitignore`

- **Purpose**: Specifies files and directories to be ignored by Git.
- **Description**: This file contains patterns that match files and directories that should not be tracked by version control, such as temporary files, build artifacts, and virtual environments.

#### `dev_destroy.py`

- **Purpose**: Script for destroying the Python development environment.
- **Description**: This script removes the virtual environment and cleans up any temporary files created during development.

#### `dev_setup.py`

- **Purpose**: Script for setting up the Python development environment.
- **Description**: This script creates the virtual environment and installs the required dependencies for development.

#### `LICENSE`

- **Purpose**: Contains the license information for the project.
- **Description**: This file provides the terms under which the project's code can be used, modified, and distributed.

#### `MANIFEST.in`

- **Purpose**: Specifies additional files to include in the source distribution.
- **Description**: This file lists non-Python files that should be included when building the package, such as documentation and configuration files.

#### `mkdocs.yml`

- **Purpose**: Configuration file for MkDocs.
- **Description**: This file defines the settings and structure for generating the project's documentation with MkDocs.

#### `pyproject.toml`

- **Purpose**: Configuration file for building the package.
- **Description**: This file contains metadata and settings for the project's build system, including dependencies, build requirements, and project information.

#### `README.md`

- **Purpose**: Provides an overview of the project.
- **Description**: This file contains a high-level description of the project, including usage instructions, installation steps, and other important information.

#### `requirements.txt`

- **Purpose**: Lists the dependencies for the project.
- **Description**: This file specifies the Python packages required for the project, which can be installed using `pip`.

#### `setup.py`

- **Purpose**: Setup script for the package.
- **Description**: This file defines the package metadata, dependencies, and entry points for installation. It is used by setuptools to build and distribute the package.

This documentation provides an overview of the files and directories in the project root, helping developers understand the structure and purpose of each item.


The `revealpack/revealpack` package contains the following files and directories:


```
revealpack/
├── _utils/
│   ├── __init__.py
│   ├── config_operations.py
│   ├── file_operations.py
│   ├── html_operations.py
│   ├── presentation_operations.py
│   └── string_operations.py
├── custom_theme/
├── build.py
├── cli.py
├── config.json
├── package.py
├── serve.py
└── setup.py
```

### File Descriptions

**`revealpack/`**

- **`_utils/`**: Directory containing utility modules for the package.
  - **`__init__.py`**: Initialization file for the `_utils` package. This file makes the directory a Python package.
  - **`config_operations.py`**: Utility functions for handling configuration operations. Includes functions for reading and validating configuration files.
  - **`file_operations.py`**: Utility functions for handling file operations. Includes functions for copying and managing files and directories.
  - **`html_operations.py`**: Utility functions for handling HTML operations. Includes functions for manipulating HTML content.
  - **`presentation_operations.py`**: Utility functions for handling presentation operations. Includes functions specific to managing Reveal.js presentations.
  - **`string_operations.py`**: Utility functions for handling string operations. Includes functions for string manipulation and formatting.

- **`custom_theme/`**: Directory for custom theme, you may use this directory to pre-package your own default theme base.

- **`build.py`**: Script for building the Reveal.js presentation package. This script compiles the presentation and prepares it for distribution.

- **`cli.py`**: Command-line interface script for the RevealPack package. Defines commands for initializing, setting up, building, serving, and packaging Reveal.js presentations.

- **`config.json`**: Configuration file for the RevealPack package. Contains settings and options for the package, including project info, directories, packages, themes, and Reveal.js configurations.

- **`package.py`**: Script for packaging the Reveal.js presentation into a distributable format. This script prepares the presentation for deployment and creates distribution packages.

- **`serve.py`**: Script for serving the Reveal.js presentations locally for live editing. This script starts a local server and watches for changes to provide live updates during development.

- **`setup.py`**: Setup script for the RevealPack package. Defines the package metadata, dependencies, and entry points for installation.

This documentation provides a comprehensive overview of the files included in the RevealPack package, helping developers understand the project structure and the purpose of each file.

## Pre-bundled Workflow: build.yml

This GitHub Actions workflow automates the build and release process for the RevealPack project. It triggers on any push to a tag matching "v*". The workflow consists of two main jobs:

1. **setup-release**: 
   - Runs on `ubuntu-latest`.
   - Creates a new GitHub release using the tag name.
   - Outputs the release upload URL for the next job.

2. **build**: 
   - Runs on `ubuntu-latest` and depends on `setup-release`.
   - Checks out the repository.
   - Sets up Python 3.12.
   - Installs project dependencies, including tools for building and publishing packages.
   - Builds the MkDocs documentation.
   - Builds the Python package.
   - Checks the built package for errors.
   - Uploads the package to PyPI.
   - Uploads the generated documentation to GitHub Pages.

This workflow ensures that every release is accompanied by an updated package on PyPI and the latest documentation on GitHub Pages.

## Building the Package

### 1. Build the Package

Use the `build` module to create the distribution files:

```sh
python -m build
```

This command will create the distribution files (both source distribution and wheel) in the `dist/` directory.

### 2. Check the Built Package

(Optional but recommended) Check the built package using `twine`:

```sh
twine check dist/*
```

## Additional Tips

- Ensure your `pyproject.toml` and `setup.py` files are correctly configured.
- Verify that the `LICENSE` and `readme.md` files are present and correctly referenced in your project.
- Consider using a virtual environment to manage dependencies and avoid conflicts.

By following these steps, you can build and publish your Python package to PyPI using modern and recommended tools and practices.
