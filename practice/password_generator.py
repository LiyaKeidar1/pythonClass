import random

print("welcome to your password generator")

chars = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'

number = int(input("amount of passwords to generate: "))

length = int(input("Input your password length: "))

print("Here are your passwords:")

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
