# `revealpack package`

## Description

The `revealpack package` command creates a distributable package of your presentations as a standalone Electron application. This allows you to distribute your presentations as desktop applications that can run independently without requiring a web server or internet connection.

## Prerequisites

**⚠️ Dart Sass CLI Required:** The `package` command may trigger builds that require Dart Sass CLI to compile SCSS/SASS theme files. If Dart Sass is not installed or not available in your system PATH, the build process will fail.

**Install Dart Sass:**
- Visit [https://sass-lang.com/install](https://sass-lang.com/install)
- Follow the installation instructions for your operating system
- Verify installation: `sass --version`

## Usage

```bash
revealpack package [OPTIONS]
```

### Options

- `--root PATH`: Root directory for the project (default: current working directory)
- `--target-dir PATH`: Output directory for the package (default: config.json `directories.package`)
- `--no-build`: Skip the build step and package existing build files
- `--clean`: Perform a clean build before packaging
- `--decks LIST`: Build and package specific decks (comma-separated values or file path)

### Examples

#### Basic Package

Create a package with all presentations:

```bash
revealpack package
```

#### Package to Specific Directory

Create a package in a custom directory:

```bash
revealpack package --target-dir /path/to/distribution
```

#### Package Without Rebuilding

Package existing build files without rebuilding:

```bash
revealpack package --no-build
```

#### Clean Build and Package

Perform a clean build before packaging:

```bash
revealpack package --clean
```

#### Package Specific Decks

Package only specific presentation decks:

```bash
revealpack package --decks "lecture-01,lecture-02"
```

#### Package from Different Directory

Package a project from a specific directory:

```bash
revealpack package --root /path/to/my/project
```

## What Gets Created

The package command creates a complete Electron application with the following structure:

```
target-directory/
├── package.json              # Node.js package configuration
├── main.js                   # Electron main process
├── .gitignore               # Git ignore file
├── README.md                # Project documentation
├── .github/
│   └── workflows/
│       └── release.yml      # GitHub Actions workflow
└── src/                     # Application source
    ├── index.html           # Main application entry point
    ├── presentations/       # Built presentations
    │   ├── lecture-01/
    │   ├── lecture-02/
    │   └── ...
    ├── assets/              # Application assets
    └── styles/              # Compiled styles
```

## Package Configuration

### package.json
The generated `package.json` includes:

```json
{
  "name": "your-project-name",
  "version": "1.0.0",
  "description": "Your project description",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "package-win": "electron-builder --win",
    "package-mac": "electron-builder --mac",
    "test": "echo \"No tests specified\" && exit 1"
  },
  "devDependencies": {
    "electron": "^31.4.0",
    "electron-builder": "^24.13.3"
  },
  "build": {
    "appId": "com.yourproject",
    "productName": "Your Project Name",
    "directories": {
      "output": "dist"
    },
    "files": [
      "src/**/*",
      "main.js"
    ],
    "win": {
      "target": "nsis",
      "icon": "assets/icons/win/icon.ico"
    },
    "mac": {
      "target": "dmg",
      "icon": "assets/icons/mac/icon.icns"
    }
  }
}
```

### main.js
The Electron main process file that:
- Creates the application window
- Loads the main HTML file
- Handles application lifecycle
- Manages window settings

### GitHub Actions Workflow
Automated build and release workflow for:
- Building on multiple platforms
- Creating release assets
- Publishing to GitHub releases

## Build Process

### 1. Build Step (Optional)
If not using `--no-build`:
- Runs `revealpack build` with specified options
- Compiles all presentations
- Processes themes and assets

### 2. File Copying
- Copies built presentations to `src/presentations/`
- Copies assets and libraries
- Preserves directory structure

### 3. Configuration Generation
- Creates `package.json` with project metadata
- Generates Electron main process file
- Creates GitHub Actions workflow
- Adds `.gitignore` and `README.md`

### 4. Asset Preparation
- Organizes files for Electron packaging
- Ensures all dependencies are included
- Validates file structure

## Distribution Options

### Desktop Applications
The packaged application can be distributed as:

#### Windows
- **NSIS Installer**: `.exe` installer with custom branding
- **Portable**: Standalone executable
- **MSI**: Windows installer package

#### macOS
- **DMG**: Disk image with drag-and-drop installation
- **PKG**: Package installer
- **App**: Standalone application bundle

#### Linux
- **AppImage**: Portable application
- **Deb**: Debian package
- **RPM**: Red Hat package

### Web Distribution
The built presentations can also be:
- Hosted on web servers
- Deployed to CDNs
- Embedded in other applications

## Configuration Options

### Project Information
Configure in `config.json`:

```json
{
  "info": {
    "authors": ["Your Name"],
    "short_title": "My Course",
    "project_title": "Advanced Topics in Computer Science",
    "year": "2024",
    "version": "1.0.0",
    "keywords": ["education", "presentations", "course"]
  }
}
```

### Package Settings
Control packaging behavior:

```json
{
  "directories": {
    "package": "dist"
  },
  "force_plugin_download": true
}
```

## Building Distributables

After packaging, you can create platform-specific distributables:

### Install Dependencies
```bash
cd target-directory
npm install
```

### Build for Windows
```bash
npm run package-win
```

### Build for macOS
```bash
npm run package-mac
```

### Build for All Platforms
```bash
npm run package-all
```

## Application Features

### Standalone Operation
- No internet connection required
- No web server needed
- Self-contained application

### Navigation
- Built-in presentation browser
- Table of contents
- Keyboard shortcuts
- Full-screen mode

### Customization
- Branded with your project information
- Custom icons and styling
- Configurable window settings

## Troubleshooting

### Build Failures
1. **Dart Sass Missing**: Install Dart Sass CLI
2. **Configuration Errors**: Check config.json syntax
3. **File Path Issues**: Verify file paths in configuration

### Package Creation Issues
1. **Permission Errors**: Ensure write access to target directory
2. **Disk Space**: Check available space for package creation
3. **File Conflicts**: Ensure target directory is empty or use different path

### Electron Build Issues
1. **Node.js Version**: Ensure compatible Node.js version
2. **Dependencies**: Run `npm install` in package directory
3. **Platform Support**: Check platform-specific requirements

### Distribution Issues
1. **Code Signing**: Required for macOS distribution
2. **Windows Certificate**: Required for Windows distribution
3. **File Size**: Large packages may need optimization

## Best Practices

### Before Packaging
1. **Test Builds**: Ensure all presentations build correctly
2. **Optimize Assets**: Compress images and optimize file sizes
3. **Update Metadata**: Verify project information in config.json
4. **Clean Build**: Use `--clean` flag for fresh builds

### Package Management
1. **Version Control**: Keep package source under version control
2. **Incremental Updates**: Use `--no-build` for quick packaging
3. **Testing**: Test packaged applications on target platforms
4. **Documentation**: Update README.md with usage instructions

### Distribution
1. **Code Signing**: Sign applications for trusted distribution
2. **Update Channels**: Set up automatic update mechanisms
3. **User Feedback**: Include feedback mechanisms in applications
4. **Analytics**: Consider adding usage analytics (with user consent)

## Advanced Usage

### Custom Electron Configuration
Modify the generated `main.js` for custom behavior:
- Window size and position
- Menu customization
- Security settings
- Update mechanisms

### Automated Distribution
Use the GitHub Actions workflow for:
- Automated builds on multiple platforms
- Release management
- Continuous deployment

### Integration with CI/CD
Integrate packaging into your build pipeline:
```bash
# In CI/CD pipeline
revealpack build --clean
revealpack package --target-dir dist
npm run package-all
```

## File Size Optimization

### Reduce Package Size
1. **Optimize Images**: Compress images and use appropriate formats
2. **Minify Assets**: Minify CSS and JavaScript files
3. **Remove Unused Files**: Clean up unused assets and libraries
4. **Use CDNs**: Consider external CDNs for large libraries

### Package Structure
Organize files efficiently:
- Separate large assets into optional downloads
- Use lazy loading for non-critical resources
- Implement progressive loading for large presentations
