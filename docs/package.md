# `revealpack package`

The `revealpack package` command sets up a new project for packaging your presentations into standalone executables using Electron. This command does not perform the actual packaging; instead, it prepares the necessary files and configurations for you to package your presentation using Electron Packager and Electron Installer.

## Overview

The `revealpack package` command copies the built presentation files to a specified destination directory and sets up the necessary project files, including `package.json`, installer configurations for both macOS and Windows, and other required assets.

## Usage

To package your presentations, navigate to your project directory and run:

```
revealpack package --dest-dir /path/to/package/directory
```

### Options

- `--root`: Root directory for packaging. Defaults to the current working directory.
- `--dest-dir`: Directory to create the package. This is required.
- `--no-build`: Skip the build step if you have already built the presentation.

Example:

```
revealpack package --root /path/to/project --dest-dir /path/to/package/directory --no-build
```

## Configuration

The packaging process relies on certain configurations specified in your `config.json` file. Below are some key configurations:

### `info`

This section provides general information about your project:

- `project_title`: The full title of your project.
- `short_title`: A short, concise title for your project.
- `version`: The current version of your project.
- `authors`: An array containing the names of the authors.

### `directories`

This section specifies the directory structure used in the project:

- `build`: Directory where the built presentation will be output (e.g., `dist`).

## Packaging Process

The following steps are executed upon running `pacakge` on a presentation project.

1. **Build the Presentation**: If the `--no-build` option is not specified, the `build.py` script is executed to build the presentation.

2. **Copy Build Directory**: The contents of the build directory specified in `config.json` are copied to the `src` subdirectory of the package directory.

3. **Create `package.json`**: A `package.json` file is generated in the package directory. This file includes metadata and scripts for packaging the application using Electron.

4. **Create Installer Configurations**:
    - **macOS**: Generates `ins-config-mac.json` for creating a macOS DMG installer.
    - **Windows**: Generates `ins-config-win.json` for creating a Windows installer.

5. **Create `.gitignore`**: A `.gitignore` file is created in the package directory to exclude unnecessary files from version control.

6. **Create GitHub Workflow**: A GitHub Actions workflow file is generated to automate the build and release process for the packaged applications.

## Notes

- A copy of the rendered presentations in the `config.directories.buil` will be created in a `src` directory specified in the `dest-dir` option.
- Ensure that all necessary files and dependencies are correctly specified in your `config.json` before packaging.
- The packaging process may take some time depending on the size of your presentations and the number of assets you've included in your presentations.

For more details on configuring and using Electron Packager after running `revealpack package`, refer to the [Electron Packager documentation](https://www.electronjs.org/docs/tutorial/application-packaging).

With these steps, you should be able to successfully set up your project for packaging your presentations into standalone applications for Windows and Mac.