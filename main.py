import os
import fnmatch
import argparse


def find_files(directory: str, filename: str, extension=None):
    matched_files = []
    for root, dirs, files in os.walk(directory):
        if filename:
            matched_files.extend(
                os.path.join(root, f) for f in files if fnmatch.fnmatch(f, filename)
            )
        elif extension:
            matched_files.extend(
                os.path.join(root, f) for f in files if f.lower().endswith(extension.lower())
            )
    return matched_files


def main():
    parser = argparse.ArgumentParser(description="Search for files similar to a filename or with a specific extension.")
    parser.add_argument('directory', help="The directory to search in")
    parser.add_argument('--filename', '-f', help="The filename pattern to search for (supports wildcards, e.g., '*.txt')")
    parser.add_argument('--extension', '-e', help="The file extension to search for (e.g., 'txt', 'py', 'jpg')")
    args = parser.parse_args()
    # Check if the user provided at least one search criterion
    if not args.filename and not args.extension:
        print("You must provide either --filename or --extension.")
        return
    # Add a wildcard to the extension for pattern matching if provided
    extension = f".{args.extension}" if args.extension and not args.extension.startswith(".") else args.extension
    matched_files = find_files(args.directory, filename=args.filename, extension=extension)
    if matched_files:
        print("Found files:")
        for file in matched_files:
            print(file)
    else:
        print("No matching files found.")


if __name__ == "__main__":
    main()