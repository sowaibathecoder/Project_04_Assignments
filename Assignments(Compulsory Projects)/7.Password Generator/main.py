# 07 : PASSWORD GENERATOR

# In this python project we will learn how to build a random password generator. You
# will collect data from the user on the number of passwords and their lengths and 
# output a collection of passwords with random characters.

import random

print("🎉 Welcome To Your Password Generator 🎊")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?1234567890'
generated_password = int(input("Enter the amount of passwords to generate: "))
length = int(input("Input your passwords length: "))

print(f"Passwords Generated: {generated_password}\nPasswords Length: {length}")

print("\n👇 Here are your passwords: ")

for pwd in range(generated_password):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)