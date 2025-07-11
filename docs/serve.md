# `revealpack serve`

## Description

The `revealpack serve` command starts a local development server with live reloading capabilities. It monitors your source files for changes and automatically rebuilds presentations when files are modified, providing a seamless development experience.

## Prerequisites

**⚠️ Dart Sass CLI Required:** The `serve` command may trigger builds that require Dart Sass CLI to compile SCSS/SASS theme files. If Dart Sass is not installed or not available in your system PATH, the build process will fail.

**Install Dart Sass:**
- Visit [https://sass-lang.com/install](https://sass-lang.com/install)
- Follow the installation instructions for your operating system
- Verify installation: `sass --version`

## Usage

```bash
revealpack serve [OPTIONS]
```

### Options

- `--root PATH`: Root directory for the project (default: current working directory)
- `--no-build`: Skip the initial build step and serve existing files only
- `--clean`: Perform a clean build before starting the server
- `--decks LIST`: Build and serve specific decks (comma-separated values or file path)

### Examples

#### Basic Serve

Start the development server with automatic rebuilding:

```bash
revealpack serve
```

#### Serve Without Initial Build

Start the server without building first (useful if you've already built):

```bash
revealpack serve --no-build
```

#### Clean Build and Serve

Perform a clean build before starting the server:

```bash
revealpack serve --clean
```

#### Serve Specific Decks

Build and serve only specific presentation decks:

```bash
revealpack serve --decks "lecture-01,lecture-02"
```

#### Serve from Different Directory

Serve a project from a specific directory:

```bash
revealpack serve --root /path/to/my/project
```

## How It Works

### 1. File Monitoring
The serve command uses a file watcher to monitor changes in your source directories:
- Watches the `source/decks/` directory for presentation content changes
- Monitors theme files and configuration changes
- Detects modifications to libraries and assets

### 2. Automatic Rebuilding
When changes are detected:
- Debounces multiple rapid changes (3-second delay)
- Prevents excessive rebuilding with a 35-second cooldown period
- Automatically runs `revealpack build` with appropriate options
- Logs build status and any errors

### 3. Local Server
Starts an HTTP server using `http-server`:
- Serves files from the build directory
- Automatically opens your default browser
- Provides live access to your presentations

## Development Workflow

### 1. Start Development Server
```bash
revealpack serve
```

### 2. Make Changes
Edit your presentation files:
- Modify HTML slides in `source/decks/`
- Update SCSS theme files
- Add or modify assets in `source/lib/`

### 3. Automatic Rebuild
The server automatically:
- Detects file changes
- Rebuilds affected presentations
- Refreshes the browser (if supported)

### 4. View Results
Your browser will show the updated presentations with your changes.

## Server Configuration

### Default Settings
- **Port**: 8000 (if available)
- **Host**: Localhost (127.0.0.1)
- **Root**: Build directory from config.json
- **Auto-open**: Browser opens automatically

### Access URLs
- **Main**: http://127.0.0.1:8000
- **Table of Contents**: http://127.0.0.1:8000/index.html
- **Individual Presentations**: http://127.0.0.1:8000/[deck-name]/

## File Watching Behavior

### Watched Directories
The server monitors:
- `source/decks/` - Presentation content
- `source/lib/` - Libraries and assets
- Theme files specified in config.json
- Configuration files

### File Types Monitored
- HTML files (`.html`)
- Markdown files (`.md`)
- SCSS/SASS files (`.scss`, `.sass`)
- JavaScript files (`.js`)
- CSS files (`.css`)
- Configuration files (`.json`)

### Ignored Files
The watcher ignores:
- Hidden files (starting with `.`)
- Temporary files
- Build output files
- Cache directories

## Build Triggers

### Automatic Triggers
The server automatically rebuilds when:
- Any file in the watched directories is modified
- Configuration files are changed
- Theme files are updated

### Manual Triggers
You can manually trigger builds by:
- Stopping and restarting the server with `--clean`
- Running `revealpack build` in another terminal

## Performance Considerations

### Debouncing
- Multiple rapid changes are debounced to prevent excessive rebuilding
- Default debounce delay: 3 seconds
- Cooldown period: 35 seconds between builds

### Build Optimization
- Only affected presentations are rebuilt
- Incremental builds when possible
- Clean builds when using `--clean` flag

## Troubleshooting

### Server Won't Start
1. **Port Already in Use**: Try a different port or stop other services
2. **Permission Issues**: Ensure you have write access to the build directory
3. **Missing Dependencies**: Install `http-server` if not available

### No Auto-Reload
1. **Browser Cache**: Hard refresh (Ctrl+F5 or Cmd+Shift+R)
2. **File Permissions**: Check file permissions in source directories
3. **Watcher Issues**: Restart the server

### Build Failures
1. **Dart Sass Missing**: Install Dart Sass CLI
2. **Configuration Errors**: Check config.json syntax
3. **File Path Issues**: Verify file paths in configuration

### Performance Issues
1. **Large Projects**: Use `--decks` to limit watched presentations
2. **Frequent Changes**: The debouncing system should handle this automatically
3. **System Resources**: Monitor CPU and memory usage

## Advanced Usage

### Custom Build Options
You can combine serve with build options:

```bash
# Serve with specific log level
revealpack serve --log-level DEBUG

# Serve with custom deck selection
revealpack serve --decks "lecture-01" --clean
```

### Integration with IDEs
The serve command works well with:
- VS Code (with live server extension)
- WebStorm
- Atom
- Any editor with file watching capabilities

### Continuous Integration
For CI/CD pipelines, use the build command instead:
```bash
revealpack build --clean
```

## Stopping the Server

To stop the development server:
- Press `Ctrl+C` in the terminal
- The server will gracefully shut down
- File watchers will be stopped
- Browser connections will be closed

## Best Practices

1. **Use Version Control**: Keep your source files under version control
2. **Regular Backups**: Backup your work regularly
3. **Test Builds**: Occasionally run `revealpack build` to ensure everything works
4. **Monitor Logs**: Watch the console output for build errors
5. **Clean Periodically**: Use `--clean` flag occasionally to ensure fresh builds