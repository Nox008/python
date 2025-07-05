import random;
import string;

print("Randon Password Generator")
length = int(input("Enter password length:"))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

allChars = letters + numbers + symbols 

password = ""

for _ in range(length):           #if no i value necessary, its better to use _
    password+=random.choice(allChars)

print("Generated Password",password)