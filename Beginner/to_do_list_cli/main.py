commands =  ['add', 'remove']
todos = []

def load_todos():
    with open("file.txt", "r") as file:
        for line in file:
            todos.append(line.strip())

def save_todos(todo):
    with open("file.txt", "a") as file:
        file.write(todo + "\n")

def update_todos():
    with open("file.txt","w") as file:
        for todo in todos:
            file.write(todo + "\n")
    
def manage_commands(user_input):
    if user_input == 'help':
        print("Command : add")
        print("add 'your to do goes here'")
        print("then a todo added in your to do list")
        print("\n\n")
        print("Command : remove")
        print("remove 'your todo index goes here you want to remove'")
        print("then a todo removed from your to do list")
        print("\n\n")
        print("Command : show")
        print("show")
        print("shows to do list")
        print("\n\n")
        print("Command : exit")
        print("exit")
        print("exit program")

    elif user_input[:3] == "add":
        todo = user_input[3:].strip()
        todos.append(todo)
        save_todos(todo)
        print("todo added successfully!!")

    elif user_input[:6] == "remove":
        todos.pop(int(user_input[6:].strip()))
        update_todos()
        print("todo removed successfully!!")

    elif user_input == "show":
        for i, line in enumerate(todos):
            print(i, line)

    else:
        print("You did something wrong")

def show_menu():
    print("-"*50)
    print("Welcome to todo".center(50))
    print("-"*50)
    print("Commands are: *add  *remove  *show  *exit")
    print("write help for help")

load_todos()
while 1:
    show_menu()
    user_input = input("Enter your command: ")
    if user_input.lower() == 'exit':
        break
    manage_commands(user_input)