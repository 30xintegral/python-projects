import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '+', '^', '%', '$']

print("Welcome to the PyPassword generator! ")
nrLetters = int(input("How many letters would you like in your password?\n"))
nrNumbers = int(input("How many numbers would you like?\n"))
nrSymbols = int(input("How many symbols would you like?\n"))

#hard level
password_list = []

for char in range(1, nrLetters+1):
    password_list.append(random.choice(letters))

for char in range(1, nrNumbers+1):
    password_list += random.choice(numbers)
    
for char in range(1, nrSymbols+1):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password =""
for char in password_list:
    password += char

print(f"Your password is: {password}")