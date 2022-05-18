# Without list comprehension
numbers = [1, 2, 3, 4, 5]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# With list comprehension
new_new_list = [n + 1 for n in numbers]
print(new_new_list)

# With strings
name = "Vinicius"
list_from_string = [letter for letter in name]
print(list_from_string)

# With range
doubled_list = [n * 2 for n in range(1, 5)]
print(doubled_list)

# With conditional
names = "Alex Beth Caroline Dave Eleanor Freddie".split(" ")
short_names = [name for name in names if len(name) < 5]
print(short_names)
screaming_names = [name.upper() for name in names if len(name) > 4]
print(screaming_names)
