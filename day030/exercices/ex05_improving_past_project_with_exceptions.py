import pandas

data_from_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data_from_csv.iterrows()}

is_on = True

while is_on:
    word = input("Enter a word: ").upper()
    try:
        code_list = [data_dict[code] for code in word]
    except KeyError:
        print("Sorry, only letters of the alphabet.")
    else:
        print(code_list)
        is_on = False
