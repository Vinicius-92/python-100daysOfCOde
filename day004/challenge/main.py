import random
import asci

options = ['rock', 'paper', 'scissors']

human_choice = input("Rock, paper or scissors? ").lower()
computer_choice = random.choice(options)

if human_choice == 'rock':
    print(asci.rock)
    if computer_choice == 'scissors':
        print("Computer choice:\n" + asci.scissors + "\nYou win.")
    elif computer_choice == 'paper':
        print("Computer choice:\n" + asci.paper + "\nYou lose.")
    else:
        print("Computer choice:\n" + asci.rock + "\nTie.")

if human_choice == 'paper':
    print(asci.paper)
    if computer_choice == 'scissors':
        print("Computer choice:\n" + asci.scissors + "\nYou lose.")
    elif computer_choice == 'paper':
        print("Computer choice:\n" + asci.paper + "\nTie.")
    else:
        print("Computer choice:\n" + asci.rock + "\nYou win.")

if human_choice == 'scissors':
    print(asci.scissors)
    if computer_choice == 'scissors':
        print("Computer choice:\n" + asci.scissors + "\nTie.")
    elif computer_choice == 'paper':
        print("Computer choice:\n" + asci.paper + "\nYou win.")
    else:
        print("Computer choice:\n" + asci.rock + "\nYou lose.")
