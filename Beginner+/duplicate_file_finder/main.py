import os
import hashlib

# Get folder path
while True:
    path = input("Enter folder path: ").strip().strip('"')

    if not path:
        print("Path cannot be empty.")
        continue

    if not os.path.exists(path):
        print("Path does not exist. Try again.")
        continue

    if not os.path.isdir(path):
        print("That path is not a folder. Try again.")
        continue

    break


file_sizes = {}

# Find files and group them by size
with os.scandir(path) as entries:

    for entry in entries:

        if entry.is_file():

            size = entry.stat().st_size

            if size not in file_sizes:
                file_sizes[size] = []

            file_sizes[size].append(entry)


# Hash only files with the same size
hashes = {}

for size, files in file_sizes.items():

    if len(files) < 2:
        continue

    for entry in files:

        hash_object = hashlib.sha256()

        with open(entry.path, "rb") as file:

            while chunk := file.read(64 * 1024):
                hash_object.update(chunk)

        file_hash = hash_object.hexdigest()

        if file_hash not in hashes:
            hashes[file_hash] = []

        hashes[file_hash].append(entry.name)


# Display duplicates
found_duplicates = False

for file_hash, files in hashes.items():

    if len(files) > 1:
        found_duplicates = True
        print("Duplicate:", files)


if not found_duplicates:
    print("No duplicate files found.")