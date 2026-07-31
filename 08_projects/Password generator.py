import random
import string

print("===== Password Generator =====")

length = int(input("Password length: "))

characters = string.ascii_letters

numbers = input("Include numbers? (y/n): ")
symbols = input("Include symbols? (y/n): ")

if numbers.lower() == "y":
    characters += string.digits

if symbols.lower() == "y":
    characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)
