import random

quotes = [
    {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs"
    },
    {
        "quote": "It always seems impossible until it's done.",
        "author": "Nelson Mandela"
    },
    {
        "quote": "Success is not final, failure is not fatal.",
        "author": "Winston Churchill"
    }
]

while True:
    quote = random.choice(quotes)

    print()
    print(quote["quote"])
    print("-", quote["author"])

    choice = input("\nPress Enter for another quote or type q to quit: ")

    if choice.lower() == "q":
        break