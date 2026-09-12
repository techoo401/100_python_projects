import os


def convert_bytes(size):

    units = ["B", "KB", "MB", "GB", "TB", "PB"]

    index = 0

    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1

    return f"{size:.2f} {units[index]}"


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


# Calculate size of every item
items = []

with os.scandir(path) as entries:

    for entry in entries:

        if entry.is_file():

            size = entry.stat().st_size
            items.append((entry.name, "file", size))

        elif entry.is_dir():

            size = 0

            for root, dirs, files in os.walk(entry.path):

                for file in files:

                    file_path = os.path.join(root, file)

                    try:
                        size += os.path.getsize(file_path)
                    except OSError:
                        pass

            items.append((entry.name, "dir", size))


# Calculate total size
dir_size = sum(item[2] for item in items)


# Display results
print("-" * 120)
print("Result".center(120))
print("-" * 120)

print(
    f"{'Name'.ljust(70)}"
    f"{'Type'.ljust(10)}"
    f"{'Size'.ljust(20)}"
    f"%"
)

print("-" * 120)


for name, item_type, size in items:

    percentage = (size / dir_size) * 100 if dir_size else 0

    print(
        f"{name.ljust(70)}"
        f"{item_type.ljust(10)}"
        f"{convert_bytes(size).ljust(20)}"
        f"{percentage:.2f}%"
    )