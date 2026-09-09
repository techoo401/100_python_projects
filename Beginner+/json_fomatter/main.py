import json

path = input("Enter JSON file path: ").strip()

try:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    print("\nValid JSON ✓")
    print("\nFormatted JSON:\n")

    print(json.dumps(data, indent=4))

except FileNotFoundError:
    print("File not found.")

except json.JSONDecodeError:
    print("Invalid JSON.")