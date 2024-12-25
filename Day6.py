import random
letters = ['a','b','c','d','e']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','%']

print("WELCOME TO PYTHON PASSWORD GENERATOR !")
no_letters=int(input(f"how many letters would you like ?\n"))
no_numbers=int(input(f"how many numbers would  you like ? \n"))
no_symbols=int(input(f"how many symbols would you like ?\n"))

password=""

for char in range(0,no_letters ):
    password += random.choice(letters)
    
for char in range(0,no_numbers):
    password += random.choice(numbers)

for char in range(0,no_symbols):
    password += random.choice(symbols)

print(password)