contact_book = {}
contact_numbers = []

def load_contacts():
    with open('contacts.txt', 'r') as file:
        for line in file:
            contact_name = line[10:].strip()
            contact_number = int(line[:10])
            contact_book[contact_number] = contact_name
            contact_numbers.append(contact_number)

def save_contact(contact_name, contact_number):
    with open("contacts.txt", "a") as file:
        file.write(str(contact_number).ljust(10) + contact_name + "\n")
    contact_numbers.append(contact_number)

def update(contact_book):
    with open("contacts.txt", "w") as file:
        for contact_number, contact_name in contact_book.items():
            file.write(str(contact_number).ljust(10) + contact_name + "\n")

def show_menu():
    print("-"*50)
    print("Welcome to Contact book".center(50))
    print("-"*50)
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Show Contacts")
    print("4. Exit")
    print("-"*50)

def add_contact(contact_name, contact_number):
    if contact_number not in contact_book:
        contact_book[contact_number] = contact_name
        save_contact(contact_name, contact_number)
    else:
        print("Contact Number already exists.")

def remove_contact(contact_number):
    del contact_book[contact_number]
    update(contact_book)

def show_contacts():
    print("-"*50)
    for i,(contact_number, contact_name) in enumerate(contact_book.items()):
            print(str(i)+". "+contact_name.ljust(40)+str(contact_number))
    print("-"*50)

def main():
    while 1:
        show_menu()
        try:
            command = int(input("Enter a digit for command: "))
        except Exception as e:
            print("please enter a valid digit.")
        
        if command == 1:
            contact_name = input("Enter Contact Name: ")

            try:
                contact_number = int(input("Enter Contact Number: "))
                if contact_number < 10e9:
                    add_contact(contact_name, contact_number)
                    print("Contact Added Successfully!!")
                else:
                    print("you are entering invalid contact number.")

            except Exception as e:
                print("please enter only digits.")

        elif command == 2:
            show_contacts()
            try:
                index = int(input("Enter index of number: "))
                if index > len(contact_book):
                    print("Please enter a valid index.")
            except Exception as e:
                print("Please enter valid index.")
            contact_number = contact_numbers[index]
            remove_contact(contact_number)
            contact_numbers.pop(index)
            print("Contact Removed Successfully!!")
            
        elif command == 3:
            show_contacts()
            
        elif command == 4:
            break
        
        else:
            print("Please Enter Valid Command.")


if __name__ == "__main__":
    load_contacts()
    main()