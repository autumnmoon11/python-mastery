from pathlib import Path

def count_files_recursive(directory: Path) -> int:
    """
    Recursively counts all files in a directory and its subdirectories.
    """
    file_count = 0
    
    for item in directory.iterdir():
        if item.is_file():
            file_count += 1
        # Filter out git files to count only actual code files
        elif item.is_dir() and item.name != ".git":
            file_count += count_files_recursive(item)
            
    return file_count

def print_tree_recursive(directory: Path, prefix: str = ""):
    """
    Prints a visual representation of the directory structure using recursion.
    """
    skip_dirs = {".git", "__pycache__", ".pytest_cache"}
    
    # Get all items in directory, but sort them (dirs first, then files)
    items = sorted(list(directory.iterdir()), key=lambda x: (not x.is_dir(), x.name))
    
    for i, item in enumerate(items):
        if item.name in skip_dirs:
            continue
            
        # Determine if this is the last item in the list for visual styling
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        print(f"{prefix}{connector}{item.name}")
        
        if item.is_dir():
            # If this dir was the last item, we add spaces; otherwise, a pipe
            extension = "    " if is_last else "│   "
            print_tree_recursive(item, prefix + extension)

if __name__ == "__main__":
    target = Path(__file__).resolve().parent.parent.parent
    print(f"Counting files in: {target}")
    total = count_files_recursive(target)
    print(f"🚀 Found {total} files total.")
    print("\n--- Project Structure ---")
    print_tree_recursive(target)