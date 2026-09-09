import csv
import os


def load_csv(path):

    with open(path, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        columns = reader.fieldnames
        rows = list(reader)

    return columns, rows


def show_columns(columns):

    print("\nColumns:")

    for index, column in enumerate(columns):
        print(f"{index}: {column}")


def show_rows(columns, rows):

    if not rows:
        print("No rows found.")
        return

    for index, row in enumerate(rows, start=1):

        values = []

        for column in columns:
            values.append(row[column])

        print(f"{index}: " + " | ".join(values))


def show_row(columns, rows):

    while True:

        try:
            number = int(input("Enter row number: "))

            if 1 <= number <= len(rows):
                break

            print("Invalid row number.")

        except ValueError:
            print("Please enter a number.")

    row = rows[number - 1]

    print()

    for column in columns:
        print(f"{column}: {row[column]}")


def search_rows(columns, rows):

    search_text = input("Enter search text: ").strip().lower()

    if not search_text:
        print("Search text cannot be empty.")
        return

    found = False

    for index, row in enumerate(rows, start=1):

        for column in columns:

            value = row[column].lower()

            if search_text in value:

                print(f"{index}: {row}")
                found = True
                break

    if not found:
        print("No matching rows found.")


def show_column(rows, columns):

    column = input("Enter column name: ").strip()

    if column not in columns:
        print("Column does not exist.")
        return

    print()

    for row in rows:
        print(row[column])


def main():

    print("=" * 40)
    print("           CSV VIEWER")
    print("=" * 40)

    while True:

        path = input("\nEnter CSV file path: ").strip()

        if not path:
            print("Path cannot be empty.")
            continue

        if not os.path.isfile(path):
            print("File does not exist.")
            continue

        if not path.lower().endswith(".csv"):
            print("File must be a CSV file.")
            continue

        break

    try:
        columns, rows = load_csv(path)

    except (OSError, csv.Error) as error:
        print(f"Could not read CSV file: {error}")
        return

    if not columns:
        print("CSV file has no columns.")
        return

    print("\nCSV loaded successfully!")
    print(f"Columns: {len(columns)}")
    print(f"Rows: {len(rows)}")

    while True:

        print("\n" + "-" * 40)
        print("1. Show columns")
        print("2. Show all rows")
        print("3. Show specific row")
        print("4. Search")
        print("5. Show column")
        print("6. Exit")
        print("-" * 40)

        choice = input("Enter choice: ").strip()

        if choice == "1":

            show_columns(columns)

        elif choice == "2":

            show_rows(columns, rows)

        elif choice == "3":

            show_row(columns, rows)

        elif choice == "4":

            search_rows(columns, rows)

        elif choice == "5":

            show_column(rows, columns)

        elif choice == "6":

            print("Goodbye!")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()