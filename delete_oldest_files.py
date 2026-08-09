from pathlib import Path

# 1. Set the folder path
folder_path = Path(r"C:\Users\Tanush\Desktop\New folder")

# 2. Gather all JSON files into a list
# (We use list() here because we need to sort them)
json_files = list(folder_path.glob('*.json'))

# 3. Sort the files by their modification time (oldest to newest)
json_files.sort(key=lambda x: x.stat().st_mtime)

# 4. Define how many of the newest files you want to KEEP
FILES_TO_KEEP = 5

# 5. Check if we exceed the limit
if len(json_files) > FILES_TO_KEEP:
    # This slices the list to get ONLY the oldest files
    files_to_delete = json_files[:-FILES_TO_KEEP]
    
    print(f"Total JSON files: {len(json_files)}")
    print(f"Keeping the {FILES_TO_KEEP} newest files. Deleting the {len(files_to_delete)} oldest...")
    print("---")
    
    # 6. Loop and delete
    for file in files_to_delete:
        print(f"Deleting: {file.name}")
        # file.unlink()  # <-- WARNING: Uncomment this line to actually delete the files!
        
else:
    print(f"You only have {len(json_files)} files. No need to delete anything.")