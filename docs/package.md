# `revealpack package`

The `revealpack package` command sets up a new project for packaging your presentations into standalone executables using Electron. This command prepares the necessary files and configurations for you to package your presentation using Electron Packager and Electron Installer. It can be run multiple times to update an existing package or create a new one from scratch.

## Overview

The `revealpack package` command copies the built presentation files to a specified destination directory and sets up the necessary project files, including `package.json`, installer configurations for both macOS and Windows, and other required assets. If the package already exists, the command updates the version number in `package.json` and cleans the target directory before copying new files.

## Usage

To package your presentations, navigate to your project directory and run:

```
revealpack package --target-dir /path/to/package/directory
```

### Options

- `--root <directory>`: Specifies the root directory for packaging. Defaults to the current working directory.
- `--target-dir <directory>`: Specifies the directory where the package will be created. Defaults to the directory specified in `config.json` under `directories.package` or `package_output` if not set.
- `--no-build`: Skips the build step. This is useful if the build has already been done and you only want to package the results.
- `--clean`: Performs a clean build before packaging. This ensures that only fresh files are included in the package.
- `--decks <file or string>`: Specifies a comma-separated list of deck names or a path to a file containing deck names to be built and included in the package. If this option is provided, a clean build is automatically performed.

Example:

```
revealpack package --root /path/to/project --target-dir /path/to/package/directory --no-build
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
- `package`: Directory where the packaged files will be output.

## Packaging Process

The following steps are executed upon running `revealpack package` on a presentation project.

1. **Build the Presentation**: If the `--no-build` option is not specified, the `build.py` script is executed to build the presentation. This step may include a clean build or the building of specific decks if the respective options are provided.

2. **Clean Target Directory**: If the target directory already exists, the `src` subdirectory is cleaned to ensure that only the fresh build output is included.

3. **Copy Build Directory**: The contents of the build directory specified in `config.json` are copied to the `src` subdirectory of the package directory.

4. **Update or Create `package.json`**: If a `package.json` file already exists in the target directory, its version number is updated based on the configuration. If it does not exist, a new `package.json` is created.

5. **Create Installer Configurations**:
    - **macOS**: Generates `ins-config-mac.json` for creating a macOS DMG installer.
    - **Windows**: Generates `ins-config-win.json` for creating a Windows installer.

6. **Create `.gitignore`**: A `.gitignore` file is created in the package directory to exclude unnecessary files from version control.

7. **Create GitHub Workflow**: A GitHub Actions workflow file is generated to automate the build and release process for the packaged applications.

## Notes

- A copy of the rendered presentations in the `config.directories.build` will be created in a `src` directory specified in the `target-dir` option.
- Ensure that all necessary files and dependencies are correctly specified in your `config.json` before packaging.
- The packaging process may take some time depending on the size of your presentations and the number of assets you've included in your presentations.

For more details on configuring and using Electron Packager after running `revealpack package`, refer to the [Electron Packager documentation](https://www.electronjs.org/docs/tutorial/application-packaging).

With these steps, you should be able to successfully set up your project for packaging your presentations into standalone applications for Windows and Mac.