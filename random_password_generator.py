import random
import string

length = int(input("Enter length of password: "))
password = ""

for _ in range(length):
    password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

print(password)