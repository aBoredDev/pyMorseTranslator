#!/usr/bin/env python

# The characters automatically defined by the package, in morse code.  Included mostly for future proofing purposes and
# in case something happens to the characters dictionary.
_morseCharacters = [
    # Letters
    '.-',
    '-...',
    '-.-.',
    '-..',
    '.',
    '..-.',
    '--.',
    '....',
    '..',
    '.---',
    '-.-',
    '.-..',
    '--',
    '-.',
    '---',
    '.--.',
    '--.-',
    '.-.',
    '...',
    '-',
    '..-',
    '...-',
    '.--',
    '-..-',
    '-.--',
    '--..',
    # Numbers
    '-----',
    '.----',
    '..---',
    '...--',
    '....-',
    '.....',
    '-....',
    '--...',
    '---..',
    '----.',
    # Punctuation
    '.-.-.-',
    '--..--',
    '..--..'
]

# The characters automatically defined by the package, in plaintext. Included mostly for future proofing purposes and
# in case something happens to the characters dictionary
_plaintextCharacters = [
    # Letters
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    # Numbers
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    # Punctuation
    '.',
    ',',
    '?'
]


class Character:
    """
    A character in both plaintext and morse code
        plaintext - The character in plaintext
        morse - The character in morse code
    """

    def __init__(self, plaintext: str, morse: str):
        self._plaintext = plaintext
        self._morse = morse

    @property
    def plaintext(self):
        return self._plaintext

    @property
    def morse(self):
        return self._morse


characters = {
    'plaintext': {
        'A': Character('A', '.-'),
        'B': Character('B', '-...'),
        'C': Character('C', '-.-.'),
        'D': Character('D', '-..'),
        'E': Character('E', '.'),
        'F': Character('F', '..-.'),
        'G': Character('G', '--.'),
        'H': Character('H', '....'),
        'I': Character('I', '..'),
        'J': Character('J', '.---'),
        'K': Character('K', '-.-'),
        'L': Character('L', '.-..'),
        'M': Character('M', '--'),
        'N': Character('N', '-.'),
        'O': Character('O', '---'),
        'P': Character('P', '.--.'),
        'Q': Character('Q', '--.-'),
        'R': Character('R', '.-.'),
        'S': Character('S', '...'),
        'T': Character('T', '-'),
        'U': Character('U', '..-'),
        'V': Character('V', '...-'),
        'W': Character('W', '.--'),
        'X': Character('X', '-..-'),
        'Y': Character('Y', '-.--'),
        'Z': Character('Z', '--..'),
        # Numbers
        '0': Character('0', '-----'),
        '1': Character('1', '.----'),
        '2': Character('2', '..---'),
        '3': Character('3', '...--'),
        '4': Character('4', '....-'),
        '5': Character('5', '.....'),
        '6': Character('6', '-....'),
        '7': Character('7', '--...'),
        '8': Character('8', '---..'),
        '9': Character('9', '----.'),
        # Punctuation
        '.': Character('.', '.-.-.-'),
        ',': Character(',', '--..--'),
        '?': Character('?', '..--..')
    },
    'morse': {
        # Letters
        '.-': Character('A', '.-'),
        '-...': Character('B', '-...'),
        '-.-.': Character('C', '-.-.'),
        '-..': Character('D', '-..'),
        '.': Character('E', '.'),
        '..-.': Character('F', '..-.'),
        '--.': Character('G', '--.'),
        '....': Character('H', '....'),
        '..': Character('I', '..'),
        '.---': Character('J', '.---'),
        '-.-': Character('K', '-.-'),
        '.-..': Character('L', '.-..'),
        '--': Character('M', '--'),
        '-.': Character('N', '-.'),
        '---': Character('O', '---'),
        '.--.': Character('P', '.--.'),
        '--.-': Character('Q', '--.-'),
        '.-.': Character('R', '.-.'),
        '...': Character('S', '...'),
        '-': Character('T', '-'),
        '..-': Character('U', '..-'),
        '...-': Character('V', '...-'),
        '.--': Character('W', '.--'),
        '-..-': Character('X', '-..-'),
        '-.--': Character('Y', '-.--'),
        '--..': Character('Z', '--..'),
        # Numbers
        '-----': Character('0', '-----'),
        '.----': Character('1', '.----'),
        '..---': Character('2', '..---'),
        '...--': Character('3', '...--'),
        '....-': Character('4', '....-'),
        '.....': Character('5', '.....'),
        '-....': Character('6', '-....'),
        '--...': Character('7', '--...'),
        '---..': Character('8', '---..'),
        '----.': Character('9', '----.'),
        # Punctuation
        '.-.-.-': Character('.', '.-.-.-'),
        '--..--': Character(',', '--..--'),
        '..--..': Character('?', '..--..')
    }
}


# The short script I used to generate the characters dictionary.  Left in in case something happens to the characters
# dictionary
# for l in range(len(_plaintextCharacters)):
#     print("'{0}': Character('{0}', '{1}'),".format(_plaintextCharacters[l], _morseCharacters[l]))
# print('')
# for l in range(len(_plaintextCharacters)):
#     print("'{1}': Character('{0}', '{1}'),".format(_plaintextCharacters[l], _morseCharacters[l]))
