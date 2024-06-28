# `revealpack serve`

The `serve` command sets up a live server to serve the built presentations, enabling live editing and automatic rebuilding when changes are detected. This command watches the specified presentation directories for changes and triggers a rebuild when necessary. It also starts an HTTP server to serve the presentations.

## Options

- `--root <directory>`: Specifies the root directory for the serve operation. Defaults to the current working directory.

## Process Overview

1. **Read and Parse Configuration:**
   The `serve` command reads the configuration options from the `config.json` file located in the specified root directory.

2. **Initialize Logging:**
   Logging is set up based on the configuration to track the server's activities and any issues that arise.

3. **Setup Watcher:**
   A watcher is set up to monitor the specified presentation directories. The watcher uses the `watchdog` library to detect changes in the file system.

4. **Trigger Build on Changes:**
   When changes are detected in the presentation files, the watcher triggers a rebuild of the presentations using the `build` command. This process is debounced to avoid multiple rapid triggers and includes a cooldown period to prevent frequent builds.

5. **Start HTTP Server:**
   An HTTP server is started to serve the presentations from the build directory. The server is configured to automatically open the default web browser to the served presentations.

## Expected Behavior

- **Live Reloading:**
  The command enables live reloading of presentations. When changes are made to the source files, the presentations are automatically rebuilt, and the changes are reflected in the browser.

- **Debounced Build Triggers:**
  The watcher debounces build triggers to prevent multiple rapid rebuilds. It ensures that only one build is triggered within the specified debounce delay and cooldown time.

- **Logging:**
  All activities, including file modifications, build triggers, and server status, are logged for debugging and tracking purposes.

- **HTTP Server:**
  The command starts an HTTP server to serve the presentations from the build directory. The server can be accessed via the default web browser.

## Example Usage

```sh
revealpack serve --root /path/to/project
```

This command will read the `config.json` from `/path/to/project`, set up a watcher on the specified presentation directories, and start an HTTP server to serve the presentations.

## Note on Watcher Configuration

The watcher monitors the directories specified in the configuration:

- **watch_directory:** The directory containing the presentation subdirectories. Defined as `<root>/config.directories.source.root/config.directories.source.presentation_root`.
- **build_directory:** The output directory for the built presentations. Defined as `<root>/config.directories.build`.

By following this process, the `serve` command ensures that the presentations are automatically rebuilt and served, providing a seamless[^1] live editing experience.

[^1]: To see changes to a current slide, you may have to refresh the browser window.
