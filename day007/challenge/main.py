import random
import ascii
import words

print(ascii.logo)
chosen_word = random.choice(words.word_list)
display = []
lives = 6
print(f'Pssst, the solution is {chosen_word}.')

for _ in range(len(chosen_word)):
    display += "_"

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:
        lives -= 1
        print("This letter is not in the word, you loose a life.")
        print(ascii.stages[lives])
    else:
        if guess in display:
            print("You already guessed this letter, try another one.")
        else:
            print("The letter you choose is in the word, good job.")
            for position in range(len(chosen_word)):
                if chosen_word[position] == guess:
                    display[position] = guess

if lives > 1:
    print("You win")
else:
    print("You loose")
print(f"{' '.join(display)}")
