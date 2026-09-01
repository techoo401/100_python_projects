import os

path = input("Enter the folder path: ").strip()

# Check whether path exists
if not os.path.exists(path):
    print("❌ Path does not exist.")
    exit()

# Check whether it is actually a directory
if not os.path.isdir(path):
    print("❌ The path is not a directory.")
    exit()

# Destination folders
folders = {
    "images": os.path.join(path, "images"),
    "videos": os.path.join(path, "videos"),
    "pdfs": os.path.join(path, "pdfs"),
    "music": os.path.join(path, "music"),
    "text_documents": os.path.join(path, "text_documents")
}

# Create folders if they don't exist
for folder in folders.values():
    os.makedirs(folder, exist_ok=True)


files = os.listdir(path)

for file in files:

    if file.lower().endswith((
        '.jpg',
        '.jpeg',
        '.png',
        '.gif',
        '.bmp',
        '.webp',
        '.tiff',
        '.tif',
        '.svg',
        '.ico'
    )):
        destination = folders["images"]

    elif file.lower().endswith((
        '.mp4',
        '.mkv',
        '.avi',
        '.mov',
        '.wmv',
        '.flv',
        '.webm'
    )):
        destination = folders["videos"]

    elif file.endswith('.mp3'):
        destination = folders["music"]

    elif file.endswith('.pdf'):
        destination = folders["pdfs"]

    elif file.endswith('.txt'):
        destination = folders["text_documents"]

    else:
        continue

    old_location = os.path.join(path, file)
    new_location = os.path.join(destination, file)

    # Handle duplicate filename
    if os.path.exists(new_location):

        name, extension = os.path.splitext(file)

        counter = 1

        while os.path.exists(new_location):
            new_file = f"{name}_{counter}{extension}"
            new_location = os.path.join(destination, new_file)
            counter += 1

    os.rename(old_location, new_location)

print("Files organized successfully!")