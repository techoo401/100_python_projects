def print_menu(menu_items):
    for i, item in enumerate(menu_items, start=1):
        print(i, ".", item)

def get_conv_data():
    start = int(input("Enter starting unit you want to convert: "))
    end = int(input("Enter final unit you want to convert: "))
    value = float(input("Enter value: "))
    return start, end, value

def cal_base(start, end, change):
    result = (change[end]/change[start])
    return result

def process(units, change):
    print_menu(units)
    start, end, value = get_conv_data()
    start, end = start-1, end-1
    base_val = cal_base(start, end, change)
    result = value * base_val
    return result

print("-"*50)
print("Welcome to Unit Converter".center(50))
print("-"*50)

print("What type of conversion you need to work on")
types_conv = ["length", "mass", "time", "temperature", "volume", "area", "derived"]
print_menu(types_conv)
selected = int(input("Choose one: "))
    
match selected:
    case 1:
        units = ["kilometer", "meter", "centimeter", "millimeter", "micrometer", "nanometer", "mile", "yard", "foot", "inch"]
        change = [0.001, 1, 100, 1000, 1000000, 1000000000, 0.000621371, 1.09361, 3.28084, 39.3701]
        result = process(units, change)
        print("Result: ",result)
    
    case 2:
        units = ["kilogram", "gram", "milligram", "microgram", "tonne", "pound", "ounce"]
        change = [0.001, 1, 1000, 1e+6, 1e-6, 0.00220462, 0.035274]
        result = process(units, change)
        print("Result: ",result)

    case 3:
        units = ["nanosecond", "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "month", "year"]
        change = [3.6e12, 3.6e9, 3.6e6, 3600, 60, 1, 1/24, 1/168, 1/730.5, 1/8766]
        result = process(units, change)
        print("Result: ",result)
    
    case 4:
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
        
    case 5:
        units = ["liter", "milliliter", "cubic_meter", "cubic_centimeter", "gallon", "quart", "pint", "cup", "fluid_ounce"]
        change = [1, 1000, 0.001, 1000, 0.264172, 1.05669, 2.11338, 4.22675, 33.814]
        result = process(units, change)
        print("Result: ", result)

    case 6:
        units = ["square_meter", "square_kilometer", "square_centimeter", "square_millimeter", "square_mile", "square_yard", "square_foot", "square_inch", "hectare", "acre"]
        change = [1, 0.000001, 10000, 1000000, 0.000000386102, 1.19599, 10.7639, 1550.0031, 0.0001, 0.000247105]
        result = process(units, change)
        print("Result: ", result)

    case 7:
        units = ["meters_per_second", "kilometers_per_hour", "miles_per_hour", "feet_per_second", "knots"]
        change = [1, 3.6, 2.23694, 3.28084, 1.94384]
        result = process(units, change)
        print("Result: ", result)