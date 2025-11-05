# TANKEKIT - Usage Guide

## Refactored Structure (3 Core Files)

The project has been refactored into a clean, modular structure with just 3 main Python files:

### Core Files

1. **`tankekit.py`** - Main application
   - Core GUI application with Qt interface
   - Software detection and removal logic
   - Built-in theme selector (5 professional themes)
   - Built-in language selector (Spanish/English)
   - Window icon support (1.ico)

2. **`database.py`** - Software database
   - 455+ entries of bloatware, adware, PUPs, and unwanted software
   - Professional justifications for each entry
   - Includes security concerns, performance impact, and privacy risks
   - Organized by categories (Games, OEM bloatware, Fake AV, etc.)

3. **`themes.py`** - Theme definitions
   - 5 professional themes: Cyberpunk 2077, PS5, Xbox 360, GTA 6, Matrix
   - Clean Qt stylesheets (CSS-compatible)
   - No unsupported properties (fixed box-shadow and content warnings)

### Support Files

- **`i18n.py`** - Internationalization support (Spanish/English)
- **`1.ico`** - Application icon file

## How to Run

### Windows

1. Double-click `tankekit.py` or run from command line:
   ```bash
   python tankekit.py
   ```

2. The application will:
   - Request administrator privileges (UAC prompt)
   - Launch with default theme and Spanish language
   - Display theme and language selectors in the main window

### Features

- **Theme Selection**: Choose from 5 professional themes via dropdown
- **Language Selection**: Switch between Spanish and English on-the-fly
- **Icon Support**: All windows and dialogs show the TANKEKIT icon
- **Detect Software**: Scans system for unwanted software using multiple methods
  - Registry scanning
  - UWP apps (PowerShell)
  - File system detection
  - WMI queries
  - Start menu shortcuts
- **Remove Software**: Aggressive removal with multiple methods
  - Terminate processes
  - Uninstall via Windows installer
  - Remove files and folders
  - Clean registry entries
  - Remove services

## Changes from Previous Version

### Fixed Issues
- ✅ Removed `box-shadow` CSS properties (not supported in Qt)
- ✅ Removed `content` CSS properties (not supported in Qt)
- ✅ Fixed `winreg.HKEY_NAMES` error (doesn't exist in Python winreg module)
- ✅ Added icon support for all windows (1.ico)
- ✅ Improved language consistency (no mixed Spanish/English)

### Improvements
- ✅ Consolidated from 11 files to 3 core files
- ✅ Integrated theme selector into main application
- ✅ Integrated language selector into main application
- ✅ Improved 82 major database entries with professional justifications
- ✅ Cleaned up code structure and removed redundancy

### Removed Files
- ❌ `bloatware_remover.py` (merged into tankekit.py)
- ❌ `bloatware_database.py` (replaced by database.py)
- ❌ `expanded_database.py` (merged into database.py)
- ❌ `launcher.py` (functionality integrated into tankekit.py)
- ❌ `tankekit_cyberpunk.py` (theme integrated)
- ❌ `tankekit_ps5.py` (theme integrated)
- ❌ `tankekit_xbox360.py` (theme integrated)
- ❌ `tankekit_gta6.py` (theme integrated)
- ❌ `tankekit_matrix.py` (theme integrated)

## Requirements

- Python 3.7+
- PySide6 (auto-installed if missing)
- psutil (auto-installed if missing)
- wmi (auto-installed if missing)
- Windows OS (uses Windows-specific APIs)

## Security Notes

⚠️ **WARNING**: This tool performs aggressive software removal operations that are irreversible.

- Always create a system restore point before using
- Review carefully what software will be removed
- Close all applications before removal
- Administrator privileges required
- Use at your own risk

## Database Categories

The database includes 455+ entries across these categories:

- **Windows Bloatware** - Pre-installed Microsoft apps rarely used
- **Games & Adware** - Pre-installed games with ads and tracking
- **Social Media Bloatware** - Facebook, TikTok, Instagram, etc.
- **Streaming Services** - Netflix, Spotify, Disney+, etc.
- **Aggressive Antivirus** - McAfee, Norton, Avast, AVG, etc.
- **Fake Antivirus** - Segurazo, SpyHunter, rogue security software
- **OEM Bloatware** - HP, Dell, Lenovo, ASUS, Acer specific software
- **Toolbars & Adware** - Ask Toolbar, Conduit, Babylon, etc.
- **System Optimizers** - CCleaner, Advanced SystemCare, etc.
- **Miscellaneous** - Other unwanted software

## License

See README.md for license information.

## Support

For issues, feature requests, or contributions, please visit the GitHub repository.
