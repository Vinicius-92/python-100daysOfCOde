from game_data import data
from random import randint
import art

points = 0


def get_register_from_data():
    value = randint(0, 50)
    return data[value]


def game(a, b):
    global points
    print(art.logo)
    if points > 0:
        print(f"You're right! Current score: {points}.")
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if a['follower_count'] > b['follower_count']:
        result = 'b'
    else:
        result = 'b'
    if answer == result:
        points += 1
        a = b
        b = get_register_from_data()
        game(a, b)
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {points}")


game(get_register_from_data(), get_register_from_data())
