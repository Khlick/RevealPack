# Assets Management

## Overview

The RevealPack build process now includes automatic copying of assets from the `assets/` directory directly to the build root directory. This allows you to include images, scripts, data files, and other resources that will be available in your final presentation.

**Benefits of this approach:**
- **Favicons and root assets**: Files like `favicon.ico` are automatically accessible at the root level
- **Cleaner paths**: No need for `src/assets/` prefix in your HTML references
- **Standard web conventions**: Follows typical web project structure where assets are at the root level
- **Easier maintenance**: Simpler path management in your presentations

## How It Works

### 1. **Automatic Asset Copying**
During the build process, the `copy_assets()` function automatically copies all contents from your project's `assets/` directory directly to the build root directory.

### 2. **Exclusion System**
Certain directories and files can be excluded from copying using regex patterns. The current exclusions are:

- `styles/` - Excluded because it's handled separately by the styles compilation system

### 3. **Recursive Copying**
The system recursively copies all subdirectories and files, maintaining the directory structure.

## Configuration

### Asset Exclusions

The system automatically excludes certain files and directories, but you can add custom exclusions through your `config.json` file.

#### Default Exclusions
The following patterns are always excluded:
- `styles/` - Handled separately by the styles compilation system
- `.git/` - Git-related files
- `.DS_Store` - macOS system files
- `Thumbs.db` - Windows thumbnail files
- `*.tmp` - Temporary files
- `*.log` - Log files

#### Custom Exclusions

Add exclusion patterns to your `config.json` file:

```json
{
  "asset_exclusions": [
    "\\.png$",            # Exclude all .png files
    "^temp_.*",           # Exclude files starting with "temp_"
    "^cache/",            # Exclude cache directories
    "\\.bak$",            # Exclude backup files
    "^draft_.*"           # Exclude draft files
  ]
}
```

**Note**: In JSON, backslashes must be escaped with double backslashes (`\\`). The patterns are treated as Python regex patterns.

### Regex Pattern Examples

| Pattern | Description | Example Files Excluded |
|---------|-------------|------------------------|
| `r"^styles$"` | Exact match for "styles" directory | `assets/styles/` |
| `r"\.png$"` | All files ending with .png | `image1.png`, `logo.png` |
| `r"^temp_.*"` | Files starting with "temp_" | `temp_file.txt`, `temp_backup.dat` |
| `r"\.log$"` | All log files | `build.log`, `error.log` |
| `r"^cache/"` | Cache directories | `assets/cache/`, `assets/cache/temp/` |

## Usage Examples

### Basic Asset Structure
```
assets/
├── favicon.ico      # Will be copied to build/favicon.ico
├── images/
│   ├── logo.png     # Will be copied to build/images/logo.png
│   └── background.jpg
├── scripts/
│   └── custom.js    # Will be copied to build/scripts/custom.js
├── data/
│   └── config.json  # Will be copied to build/data/config.json
├── ext/
│   ├── plugin.js    # Will be copied to build/ext/plugin.js
│   └── styles.css   # Will be copied to build/ext/styles.css
└── styles/          # Excluded - handled separately
    └── custom.scss
```

### Build Output
After building, your assets will be available at:
```
build/
├── images/
│   ├── logo.png
│   └── background.jpg
├── scripts/
│   └── custom.js
├── data/
│   └── config.json
├── file.ico
└── ext/
    └── ...
```

## Integration with Presentations

Assets copied to the build root are available for use in your HTML presentations:

```html
<!-- Image from assets -->
<img src="images/logo.png" alt="Logo">

<!-- Script from assets -->
<script src="scripts/custom.js"></script>

<!-- Data file from assets -->
<script>
    fetch('data/config.json')
        .then(response => response.json())
        .then(data => console.log(data));
</script>

<!-- Root-level assets -->
<link rel="icon" href="file.ico">
```

## Best Practices

1. **Organize assets logically** - Use subdirectories to group related assets
2. **Keep assets lightweight** - Large files can slow down build and presentation loading
3. **Use appropriate exclusions** - Exclude temporary files, build artifacts, and other unnecessary content
4. **Version control** - Include assets in your project repository for consistent builds
5. **Use configuration-based exclusions** - Keep exclusion patterns in `config.json` for easy maintenance

## Practical Examples

### Example 1: Excluding Image Formats
If you want to exclude all image files from being copied:

```json
{
  "asset_exclusions": [
    "\\.png$",
    "\\.jpg$",
    "\\.jpeg$",
    "\\.gif$",
    "\\.svg$"
  ]
}
```

### Example 2: Excluding Development Files
Exclude development and temporary files:

```json
{
  "asset_exclusions": [
    "^dev_",
    "^temp_",
    "\\.dev$",
    "\\.test$",
    "^cache/"
  ]
}
```

### Example 3: Excluding Specific Directories
Exclude entire directories that aren't needed in production:

```json
{
  "asset_exclusions": [
    "^source_files/",
    "^documentation/",
    "^examples/"
  ]
}
```

## Troubleshooting

### Assets Not Copying
- Check that the `assets/` directory exists in your project root
- Verify that files aren't being excluded by regex patterns
- Check build logs for any error messages

### Performance Issues
- Exclude large files or directories that aren't needed in the final presentation
- Use appropriate image formats and compression
- Consider lazy loading for large assets

### Path Issues
- Assets are copied directly to the build root directory
- Use relative paths from the presentation root (e.g., `images/logo.png`, `scripts/custom.js`)
- Test paths in the built presentation, not the source files

### Configuration Issues
- Ensure `asset_exclusions` is a list of strings in your `config.json`
- Regex patterns must be valid Python regex syntax
- Check build logs for any regex compilation errors
- Verify that exclusion patterns are working as expected by checking debug logs
