from random import randint
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Type 'easy' or 'hard': ")

number = randint(0, 101)
attempts = 0
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < number:
        print("To low.")
        attempts -= 1
    elif guess > number:
        print("To high.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number}.")
        exit()
print(f"You loose, the answer was {number}.")
