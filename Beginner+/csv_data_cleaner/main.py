import csv
import os


def load_csv(path):
    """Load CSV data and return columns and rows."""

    with open(path, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        columns = reader.fieldnames
        rows = list(reader)

    return columns, rows


def clean_value(value):
    """Remove leading and trailing whitespace."""

    if value is None:
        return ""

    return value.strip()


def clean_rows(rows, columns):
    """Clean whitespace and remove completely empty rows."""

    cleaned_rows = []
    empty_rows = 0

    for row in rows:

        cleaned_row = {}

        for column in columns:
            cleaned_row[column] = clean_value(row.get(column, ""))

        # Check whether the entire row is empty
        if all(value == "" for value in cleaned_row.values()):
            empty_rows += 1
            continue

        cleaned_rows.append(cleaned_row)

    return cleaned_rows, empty_rows


def remove_duplicates(rows, columns):
    """Remove duplicate rows while preserving order."""

    unique_rows = []
    seen = set()
    duplicate_rows = 0

    for row in rows:

        # Convert row values into a tuple
        row_data = tuple(row[column] for column in columns)

        if row_data in seen:
            duplicate_rows += 1
            continue

        seen.add(row_data)
        unique_rows.append(row)

    return unique_rows, duplicate_rows


def save_csv(path, columns, rows):
    """Save cleaned data to a new CSV file."""

    with open(path, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=columns)

        writer.writeheader()
        writer.writerows(rows)


def main():

    print("=" * 50)
    print("CSV DATA CLEANER")
    print("=" * 50)

    # Get CSV path
    path = input("Enter CSV file path: ").strip()

    # Validate path
    if not os.path.isfile(path):
        print("Error: File does not exist.")
        return

    # Validate extension
    if not path.lower().endswith(".csv"):
        print("Error: Please provide a CSV file.")
        return

    try:

        # Load CSV
        columns, rows = load_csv(path)

    except PermissionError:
        print("Error: Permission denied.")
        return

    except UnicodeDecodeError:
        print("Error: Could not read the file encoding.")
        return

    except csv.Error:
        print("Error: Invalid CSV file.")
        return

    # Check whether CSV has columns
    if not columns:
        print("Error: CSV file does not contain columns.")
        return

    print("\nCleaning CSV...")

    original_count = len(rows)

    # Clean whitespace and empty rows
    cleaned_rows, empty_rows = clean_rows(rows, columns)

    # Remove duplicates
    cleaned_rows, duplicate_rows = remove_duplicates(
        cleaned_rows,
        columns
    )

    # Create output filename
    directory = os.path.dirname(path)
    filename = os.path.basename(path)

    name, extension = os.path.splitext(filename)

    output_filename = f"{name}_cleaned{extension}"

    output_path = os.path.join(
        directory,
        output_filename
    )

    # Save cleaned CSV
    try:

        save_csv(
            output_path,
            columns,
            cleaned_rows
        )

    except PermissionError:
        print("Error: Permission denied while saving file.")
        return

    # Summary
    final_count = len(cleaned_rows)

    print("\n" + "=" * 50)
    print("CLEANING COMPLETE")
    print("=" * 50)

    print(f"Original rows : {original_count}")
    print(f"Empty rows    : {empty_rows}")
    print(f"Duplicates    : {duplicate_rows}")
    print(f"Final rows    : {final_count}")

    print(f"\nCleaned file saved to:")
    print(output_path)


if __name__ == "__main__":
    main()