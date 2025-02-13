
print("Welcome to Password generator")
import random

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '#', ]

let = int(input("How many letters you want?\n"))
sym = int(input("How many symbols do you want?\n"))
num = int(input("How many numbers do you want?\n"))

# password = ""
#
# for char in range(0, let):
#     password += random.choice(alphabets)
# for char in range(0, sym):
#     password += random.choice(symbols)
# for char in range(0, num):
#     password += random.choice(str(numbers))
#
# print(password)
#

password_list= []

for char in range(0, let):
    password_list.append(random.choice(alphabets))
for char in range(0, sym):
    password_list.append(random.choice(symbols))
for char in range(0, num):
    password_list.append(random.choice(str(numbers)))

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""

for char in password_list:
    password+=char
print(f"Your Password is : {password}")

