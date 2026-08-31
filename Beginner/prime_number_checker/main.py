num = int(input("Enter your number: "))

if num < 2:
    print(num, "is not a prime number.")

elif num == 2:
    print(num, "is a prime number.")

elif num % 2 == 0:
    print(num, "is not a prime number.")

else:
    prime = True

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")