from datetime import date
import json

# negative balance allowed
balance = 0
balance_record = []


def add_expense(expense_name, expense_amount):
    global balance

    record_data = {}
    record_data["type"] = "Expense"
    record_data["expense_name"] = expense_name
    record_data["amount"] = expense_amount
    record_data["date"] = str(date.today())

    balance_record.append(record_data)

    balance -= expense_amount
    print("Expense added")


def add_amount(asset_name, amount):
    global balance

    record_data = {}
    record_data["type"] = "Asset"
    record_data["asset_name"] = asset_name
    record_data["amount"] = amount
    record_data["date"] = str(date.today())

    balance_record.append(record_data)

    balance += amount
    print("Amount added")


def load_data():
    global balance_record
    global balance

    with open("record.json", "r", encoding="utf-8") as file:
        balance_record = json.load(file)

    with open("balance.txt", "r", encoding="utf-8") as file:
        balance = int(file.read().strip())


def save_data():
    with open("record.json", "w", encoding="utf-8") as file:
        json.dump(balance_record, file, indent=4)

    with open("balance.txt", "w", encoding="utf-8") as file:
        file.write(str(balance))


load_data()

while True:
    print("-" * 50)
    print("Welcome to Expense Tracker".center(50))
    print("-" * 50)

    print("1. Add Amount")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show Records")
    print("5. Exit")

    try:
        command = int(input("Enter your choice: "))
    except Exception:
        print("Please Enter a valid choice")
        continue

    if command == 1:
        asset_name = input("Enter asset name: ")
        amount = int(input("Enter amount: "))

        add_amount(asset_name=asset_name, amount=amount)

    elif command == 2:
        expense_name = input("Enter expense name: ")
        amount = int(input("Enter amount: "))

        add_expense(
            expense_name=expense_name,
            expense_amount=amount
        )

    elif command == 3:
        print("Your Balance:", balance)

    elif command == 4:
        print("Your Balance Record:")

        for record in balance_record:
            name = 'asset_name' if record['type'] == 'Asset' else 'expense_name'
            print(record['type'].ljust(20)+record[name].ljust(50)+str(record['amount']).ljust(20)+record['date'])

    elif command == 5:
        break

    else:
        print("Please enter a valid command.")

save_data()