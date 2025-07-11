# `revealpack init`

## Description

The `revealpack init` command initializes a new RevealPack project by creating the essential configuration file and copying necessary assets to your project directory. This is the first step in setting up a RevealPack project.

## Usage

```bash
revealpack init [--destination PATH]
```

### Options

- `--destination PATH` (optional): The destination directory where the project should be initialized. If not provided, the current working directory will be used.

### Examples

#### Initialize in Current Directory

To initialize a RevealPack project in the current directory:

```bash
revealpack init
```

#### Initialize in Specific Directory

To initialize a RevealPack project in a specific directory:

```bash
revealpack init --destination /path/to/my/project
```

## What Gets Created

When you run `revealpack init`, the following files and directories are created:

### 1. `config.json`
A comprehensive configuration file that controls all aspects of your RevealPack project:

```json
{
  "info": {
    "authors": ["Your Name"],
    "short_title": "Lectures",
    "project_title": "Science Lectures",
    "year": "2024",
    "version": "1.0.0"
  },
  "directories": {
    "build": "build",
    "package": "dist",
    "source": {
      "root": "source",
      "presentation_root": "decks",
      "libraries": "lib"
    }
  },
  "packages": {
    "reveal.js": "5.1.0",
    "reveal_plugins": {
      "built_in": ["notes", "highlight", "math"],
      "external": {}
    }
  },
  "theme": "simple",
  "reveal_configurations": {
    "center": false,
    "controls": true,
    "transition": "fade"
  }
}
```

### 2. `assets/` Directory
Contains RevealPack's built-in assets and resources:
- Default themes and styles
- Template files
- Utility scripts

## Configuration Customization

After initialization, you should customize the `config.json` file for your specific project:

### Project Information
```json
{
  "info": {
    "authors": ["Your Name", "Co-Author"],
    "short_title": "My Course",
    "project_title": "Advanced Topics in Computer Science",
    "year": "2024",
    "version": "1.0.0",
    "keywords": ["computer science", "algorithms", "data structures"]
  }
}
```

### Directory Structure
You can customize the directory structure to match your preferences:

```json
{
  "directories": {
    "build": "output",
    "package": "distribution",
    "source": {
      "root": "src",
      "presentation_root": "presentations",
      "libraries": "assets"
    }
  }
}
```

### Reveal.js Configuration
Configure Reveal.js version and plugins:

```json
{
  "packages": {
    "reveal.js": "5.2.1",
    "reveal_plugins": {
      "built_in": ["notes", "highlight", "math", "zoom"],
      "external": {
        "reveal-chart": {
          "version": "1.0.0",
          "url": "https://github.com/example/reveal-chart/releases/download/v1.0.0/reveal-chart.zip"
        }
      }
    }
  }
}
```

**Note:** RevealPack is tested with Reveal.js 5.2.1 and is backwards compatible with Reveal.js 4.x versions.

### Theme Settings
Configure your presentation theme:

```json
{
  "theme": "custom-theme.scss",
  "highlight_theme": "monokai",
  "custom_scripts": ["src/scripts/custom.js"]
}
```

### Reveal.js Options
Customize Reveal.js behavior:

```json
{
  "reveal_configurations": {
    "center": true,
    "controls": true,
    "controlsBackArrows": "faded",
    "controlsLayout": "bottom-right",
    "transition": "slide",
    "transitionSpeed": "fast",
    "width": 1920,
    "height": 1080,
    "margin": 0.1,
    "minScale": 0.2,
    "maxScale": 1.5
  }
}
```

## Next Steps

After running `revealpack init`, proceed with:

1. **Customize Configuration**: Edit `config.json` to match your project requirements
2. **Setup Environment**: Run `revealpack setup` to create directories and download dependencies
3. **Create Content**: Add your presentation content to the source directories
4. **Build Presentations**: Use `revealpack build` to compile your presentations

## File Structure After Init

```
your-project/
├── config.json          # Project configuration
└── assets/              # RevealPack assets
    ├── styles/
    ├── templates/
    └── ...
```

## Troubleshooting

### Permission Errors
If you encounter permission errors when creating files:
- Ensure you have write permissions in the destination directory
- Try running with elevated privileges if necessary

### File Already Exists
If `config.json` already exists:
- The existing file will be backed up with a `.bak` extension
- A new `config.json` will be created with default settings

### Assets Directory Issues
If the `assets/` directory cannot be created:
- Check available disk space
- Verify directory permissions
- Ensure the destination path is valid

## Best Practices

1. **Use Version Control**: Initialize a git repository after running `revealpack init`
2. **Backup Configuration**: Keep backups of your `config.json` file
3. **Document Changes**: Comment your configuration changes for future reference
4. **Test Configuration**: Run `revealpack setup` to validate your configuration