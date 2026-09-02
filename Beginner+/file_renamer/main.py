import os

# Get directory path
while True:
    path = input("Enter directory path: ").strip().strip('"')

    if not path:
        print("Path cannot be empty.")
        continue

    if not os.path.exists(path):
        print("Directory does not exist.")
        continue

    if not os.path.isdir(path):
        print("That path is not a directory.")
        continue

    break


# Get files and directories
files_and_dirs = os.listdir(path=path)

if not files_and_dirs:
    print("Directory is empty.")
    exit()


print("\nWhich file or directory do you want to rename?")
print("-" * 50)

for i, item in enumerate(files_and_dirs):

    filetype = (
        "file"
        if os.path.isfile(os.path.join(path, item))
        else "dir"
    )

    print(str(i).ljust(10), filetype.ljust(10), item)


# Get valid index
while True:
    try:
        choice = int(input("\nEnter by index: "))

        if choice < 0 or choice >= len(files_and_dirs):
            print("Invalid index. Please choose an index from the list.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")


# Get new name
while True:
    new_name = input("Enter new name: ").strip()

    if not new_name:
        print("New name cannot be empty.")
        continue

    # Check if the new name already exists
    new_path = os.path.join(path, new_name)

    if os.path.exists(new_path):
        print("A file or directory with that name already exists.")
        continue

    break


# Rename
old_path = os.path.join(path, files_and_dirs[choice])

try:
    os.rename(old_path, new_path)
    print("Task Done Successfully!!")

except OSError as e:
    print(f"Rename failed: {e}")