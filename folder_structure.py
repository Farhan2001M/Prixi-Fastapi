from pathlib import Path

def get_folder_structure(path, level=2, current_level=1, exclude_folders=None):
    if current_level > level:
        return
    
    if exclude_folders is None:
        exclude_folders = []

    # Create a Path object
    p = Path(path)
    
    # Iterate over items in the directory
    for item in p.iterdir():
        # If the item is a directory and should be excluded, only print the folder name
        if item.is_dir() and item.name in exclude_folders:
            print("  " * (current_level - 1) + item.name)
        
        # If it's not excluded or is a file, print the item
        elif item.is_dir() and item.name not in exclude_folders:
            print("  " * (current_level - 1) + item.name)
            get_folder_structure(item, level, current_level + 1, exclude_folders)
        
        # If it's a file, print the file name
        elif item.is_file():
            print("  " * (current_level - 1) + item.name)

# Replace 'your_folder_path' with the path of the folder you want to inspect
folder_path = r'F:\Learning\Prixi-fastapi'

# List of folders to exclude from listing their contents
exclude_folders = ['.git', '.next', 'node_modules']

get_folder_structure(folder_path, exclude_folders=exclude_folders)
