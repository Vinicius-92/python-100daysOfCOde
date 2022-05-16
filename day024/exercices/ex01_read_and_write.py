with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("Testing write appending a result to existing file.")

with open("my_file.txt", mode="w") as file:
    file.write("Testing write erasing existing content and replacing it.")

with open("new_file.txt", mode="w") as file:
    file.write("Testing write creating new file.")

with open("/home/viniciussilva/Área de Trabalho/another_file.txt") as file:
    contents = file.read()
    print(contents)

with open("./../../../Área de Trabalho/another_file.txt") as file:
    contents = file.read()
    print(contents)
