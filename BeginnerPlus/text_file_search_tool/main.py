import os


# Get directory path
while True:
    path = input("Enter directory path: ").strip()

    if not path:
        print("Path cannot be empty.")
        continue

    if not os.path.isdir(path):
        print("Directory does not exist. Try again.")
        continue

    break


# Get search text
while True:
    search_text = input("Enter text to search: ")

    if not search_text.strip():
        print("Search text cannot be empty.")
        continue

    break


print("\nSearching...\n")

found = False


# Walk through directory and all subdirectories
for root, dirs, files in os.walk(path):

    for filename in files:

        file_path = os.path.join(root, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as file:

                for line_number, line in enumerate(file, start=1):

                    if search_text.lower() in line.lower():

                        if not found:
                            print("Found in:\n")

                        found = True

                        print(f"{file_path}")
                        print(f"   Line {line_number}: {line.strip()}")

        except (UnicodeDecodeError, PermissionError, OSError):
            # Skip files that cannot be read
            continue


if not found:
    print("Text not found.")