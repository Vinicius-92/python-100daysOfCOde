# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pass_letters = ""
pass_sym = ""
pass_num = ""
while len(pass_letters) < nr_letters:
    position = random.randint(0, len(letters) - 1)
    pass_letters += letters[position]

while len(pass_sym) < nr_symbols:
    position = random.randint(0, len(symbols) - 1)
    pass_sym += symbols[position]

while len(pass_num) < nr_numbers:
    position = random.randint(0, len(numbers) - 1)
    pass_num += numbers[position]

password = pass_letters + pass_sym + pass_num

shuffled = list(password)
random.shuffle(shuffled)
result = ''.join(shuffled)

print(result)

