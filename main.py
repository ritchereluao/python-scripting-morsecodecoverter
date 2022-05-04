MORSE_CODES = {"A": "._", "B": "_...", "C": "_._.", "D": "_..", "E": ".", "F": ".._.", 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', "1": ".____",
              }

message = input('Enter String: ')


def convertmorsecode(message):
    code = []
    for letter in message.upper():
        if letter in MORSE_CODES:
            code.append(MORSE_CODES[letter])
        else:
            code.append(" ")
    return " ".join(code)


print(convertmorsecode(message))
