# FileNotFound
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    # print(a_dict["ahoy!"])
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Ahoy!")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    raise KeyError("This is an error that I made up")
