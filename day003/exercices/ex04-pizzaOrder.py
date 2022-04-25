# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

pizza_prices = {'S': 15, 'M': 20, 'L': 25}
pepperoni_prices = {'S': 2, 'M': 3, 'L': 3}

bill = pizza_prices.get(size)
if add_pepperoni == 'Y':
    bill += pepperoni_prices.get(size)
if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")
