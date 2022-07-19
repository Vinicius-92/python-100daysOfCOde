decoder = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}


def convert(message: str):
    output = ''
    for char in message:
        if char == ' ':
            output += '/'
        else:
            output += f'{decoder[char.upper()]} '
    print(output[:-1])


print('Welcome to the morse code converter\n')
run = True
while run:
    m = input('Enter the text you wish to convert (only the 26 letters and 10 digits are allowed): ')
    convert(m)
    again = input('\nWould you like to convert something else? (enter y/n): ')
    if again == 'n':
        run = False
