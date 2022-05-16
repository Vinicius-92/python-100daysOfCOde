with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    start_letter = letter_file.read()

for name in names:
    new_letter = start_letter.replace("[name]", name.strip())
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as letter:
        letter.write(new_letter)
