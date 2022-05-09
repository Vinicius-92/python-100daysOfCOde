from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)
table.align = "l"
table.add_row(["Psyduck", "Psychic"])
print(table)
