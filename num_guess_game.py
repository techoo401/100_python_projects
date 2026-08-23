import random

target = random.randint(1,100)
tries = 0

while True:
    guess = int(input("Guess the number: "))
    tries += 1

    if guess > target:
        print("Guess Lower")
    elif guess < target:
        print("Guess Higher")
    else:
        print("you won. you guessed the number in ", tries, "attemps.")
        break