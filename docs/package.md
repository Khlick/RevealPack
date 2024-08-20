markdown_content = """
# `revealpack package`

The `revealpack package` command sets up a project for packaging your presentations into standalone executables using Electron. This command handles the necessary files and configurations for packaging your presentation with Electron Builder. It can be used multiple times to update an existing package or create a new one from scratch.

## Overview

The `revealpack package` command copies the built presentation files to a specified destination directory and sets up essential project files, including `package.json`, installer configurations for macOS and Windows, and other assets. If the package already exists, the command updates relevant metadata, such as the version number, in `package.json` and cleans the target directory to ensure only the latest files are included.

## Usage

To package your presentations, navigate to your project directory and run:

```sh
revealpack package --target-dir /path/to/package/directory
```

### Options

- `--root <directory>`: Specifies the root directory for packaging. Defaults to the current working directory.
- `--target-dir <directory>`: Specifies the directory where the package will be created. Defaults to the directory specified in `config.json` under `directories.package` or `package_output`.
- `--no-build`: Skips the build step, useful if the build has already been completed and you only need to package the results.
- `--clean`: Performs a clean build before packaging, ensuring that only fresh files are included.
- `--decks <file or string>`: Specifies a comma-separated list of deck names or a path to a file containing deck names to be built and included in the package. This triggers an automatic clean build.

Example:

```sh
revealpack package --root /path/to/project --target-dir /path/to/package/directory --no-build
```

## Configuration

The packaging process relies on configurations specified in your `config.json` file. Below are key configurations:

### `info`

- `project_title`: The full title of your project.
- `short_title`: A concise title for your project.
- `version`: The current version of your project.
- `authors`: An array containing the names of the authors.

### `directories`

- `build`: Directory where the built presentation will be output (e.g., `dist`).
- `package`: Directory where the packaged files will be output.

## Packaging Process

1. **Build the Presentation**: If `--no-build` is not specified, the `build.py` script runs to build the presentation. This may include a clean build or building specific decks if those options are provided.
   
2. **Clean Target Directory**: If the target directory exists, the `src` subdirectory is cleaned to ensure only fresh build outputs are included.
   
3. **Copy Build Directory**: The contents of the build directory specified in `config.json` are copied to the `src` subdirectory of the package directory.
   
4. **Update or Create `package.json`**: If a `package.json` file exists in the target directory, its metadata (such as version number) is updated. If not, a new `package.json` is created with all necessary information for Electron Builder.
   
5. **Create `.gitignore`**: A `.gitignore` file is created to exclude unnecessary files from version control.
   
6. **Create GitHub Workflow**: A GitHub Actions workflow file is generated to automate the build and release process for the packaged applications.

## Notes

- The rendered presentations in the `config.directories.build` will be copied to a `src` directory in the `target-dir`.
- Ensure all necessary files and dependencies are correctly specified in `config.json` before packaging.
- The packaging process may take time depending on the size of your presentations and the number of assets included.

For more details on configuring and using Electron Builder after running `revealpack package`, refer to the [Electron Builder documentation](https://www.electron.build/).

With these steps, you can set up your project to package your presentations into standalone applications for Windows and macOS.

### Next Steps

Once the package directory is created and populated with the necessary files, review the `package.json` and update any metadata or build steps as needed. Inspect the workflow file in the `.github/workflows` directory to understand how to bundle the presentation with Electron Builder. 

Add your custom icons in the `assets/icons/[mac/win]` directories depending on your target OS. If you choose not to use custom icons, you can remove the icon field from the `package.json`.

### Local and GitHub Builds

- To generate installers locally, navigate to the package directory, run `npm install`, and then run the command for your OS:
  - `npm run package-win` for Windows
  - `npm run package-mac` for macOS
- To automate the process with GitHub Actions, initialize a git repository, push a tag to GitHub, and the application will generate a new release and build installers for both macOS and Windows.
"""
