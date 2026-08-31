fibonacci = [1, 1]

while True:
    try:
        length = int(input("Enter length of Fibonacci series: "))

        if length <= 0:
            print("Length must be greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")


if length >= 1:
    print(fibonacci[0])

if length >= 2:
    print(fibonacci[1])


for _ in range(2, length):
    next_number = fibonacci[-1] + fibonacci[-2]

    fibonacci.append(next_number)
    fibonacci.pop(0)

    print(fibonacci[-1])