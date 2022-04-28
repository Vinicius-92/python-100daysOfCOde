# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

true = ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']
names = name1.lower() + name2.lower()
true_count, love_count = 0, 0
for letter in true:
    true_count += names.count(letter)
for letter in love:
    love_count += names.count(letter)
score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
