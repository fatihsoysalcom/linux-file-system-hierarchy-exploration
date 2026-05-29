import os

def explore_directory(path, indent=0, max_depth=2):
    """Recursively explores a directory and prints its structure."""
    if indent > max_depth:
        return

    try:
        # List all entries in the current directory
        entries = os.listdir(path)
        entries.sort() # Sort for consistent output
    except PermissionError:
        print(f"{'  ' * indent}- {os.path.basename(path)} [Permission Denied]")
        return
    except FileNotFoundError:
        print(f"{'  ' * indent}- {os.path.basename(path)} [Not Found]")
        return

    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            # If it's a directory, print its name and recurse
            print(f"{'  ' * indent}+ {entry}/")
            explore_directory(full_path, indent + 1, max_depth)
        else:
            # If it's a file, just print its name
            print(f"{'  ' * indent}- {entry}")

if __name__ == "__main__":
    print("Exploring Linux File System Hierarchy (starting from root, max depth 2):")
    # Start exploration from the root directory '/'
    explore_directory('/')
