def print_menu(menu_items):
    for i, item in enumerate(menu_items, start=1):
        print(i, ".", item)

def get_conv_data():
    start = int(input("Enter starting unit you want to convert: "))
    end = int(input("Enter final unit you want to convert: "))
    value = float(input("Enter value: "))
    return start, end, value

print("="*50)
print("Welcome to Temperature converter".center(50))
print("="*50)

units = ["celsius", "fahrenheit", "kelvin"]
print_menu(units)
start, end, value = get_conv_data()
if(start == 1 and end == 2):
    result = (value * 1.8) + 32
    print("Result: ", result)
elif (start == 1 and end == 3):
    result = value + 273.15
    print("Result: ", result)
elif (start == 2 and end == 1):
    result = (value -32) * (5/9)
    print("Result: ", result)
elif (start == 2 and end == 3):
    result = (value -32) * (5/9) + 273.15
    print("Result: ", result)
elif (start == 3 and end == 1):
    result = value - 273.15
    print("Result: ", result)
elif (start == 3 and end == 2):
    result = (value - 273.15) * (9/5) + 32
    print("Result: ", result)
else:
    print("Result: ", value)