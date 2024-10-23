# File Browser CLI

This is a command line tool that can search for files within a specified directory by name and/or extension.

## Prerequisites

- Python 3.7 or higher
- `fnmatch` library for file name matching.

Install `fnmatch` using:
```bash
pip install fnmatch
```

## Getting Started

```bash
git clone https://github.com/Harmones81/File-Browser-CLI.git
cd Background-Remover-CLI
```

### Usage

1. **Search for a file by name**
   ```bash
   python main.py path/to/search/directory -f filename
   ```
   This will return a list of files with a similar name to the file name
3. **Search for a file by extension**
   ```bash
   python main.py path/to/search/directory -e extension
   ```
   This will return a list of files with the specified extension
5. **Search for a file by name and extension**
   ```bash
   python main.py path/to/search/directory -f *filename*.extension (ex: *report*.txt)
   ```
   This will return a list of files that contain the filename and the specified extension
