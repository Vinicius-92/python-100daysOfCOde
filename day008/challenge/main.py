from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
running = True


def caesar(message, number, action):
    result = ""
    if action.lower() == "encode":
        for letter in message:
            if letter in alphabet:
                new_index = alphabet.index(letter.lower()) + number
                if new_index > 25:
                    new_index -= len(alphabet)
                result += alphabet[new_index]
            else:
                result += letter
    else:
        for letter in message:
            if letter in alphabet:
                new_index = alphabet.index(letter.lower()) - number
                if new_index < 0:
                    new_index += len(alphabet)
                result += alphabet[new_index]
            else:
                result += letter
    print(f"The {action}d text is {result}")


while running:
    direction = input("Type 'encode' to encrypt, type 'decode to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type your shift number:\n"))
    while shift > 25:
        shift = shift % 26

    caesar(text, shift, direction)
    user_answer = input("Want to continue using the program? Yes or no? ").lower()
    if user_answer == "no":
        running = False

print("Goodbye 👋")
