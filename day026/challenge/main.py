import pandas

# Create a dictionary in this format:
data_from_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data_from_csv.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
code_list = [data_dict[code] for code in word]
print(code_list)
