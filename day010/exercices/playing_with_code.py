name = input("Insert your first and last name: ").title().split(" ")


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    return f"{f_name} {l_name}"


print(format_name(name[0], name[1]))
