while True:
    try:
        num = int(input("Enter number of table: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

for i in range(1, 11):
    print(num, "x", i, "=", num * i)