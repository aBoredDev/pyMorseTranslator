#!/usr/bin/env python
from pyMorse import character


class Message:
    """
    An intermediate class used to simplify encoding and decoding of messages
        plaintext: string
        morse: string
    """

    def __init__(self):
        # The plaintext version of the message
        self.plaintext = ''
        # The morse-encoded version of the message
        self.morse = ''


class Encoder:
    """
    A set of methods to encode plaintext strings into morse code
    """

    def __init__(self, **kwargs):
        # Define the dot, dash and separator symbols
        try:
            self.dot = kwargs['dot']
        except KeyError:
            self.dot = '.'

        try:
            self.dash = kwargs['dash']
        except KeyError:
            self.dash = '-'

        try:
            self.separator = kwargs['separator']
        except KeyError:
            self.separator = '/'

        # Initialize the previousMessage value
        self._previousMessage = Message()

    def encode(self, plaintext: str):
        # Set the plaintext value of the previousMessage attribute
        self._previousMessage.plaintext = plaintext

        # Split the message into individual characters
        message = list(plaintext.upper())

        for char in message:
            if char == ' ':
                self._previousMessage.morse += '%s ' % self.separator
            else:
                try:
                    self._previousMessage.morse += character.characters['plaintext'][char].morse
                except KeyError:
                    raise ValueError('%s is not defined as a character!  Please wait foe the developer to add the'
                                     'ability to add custom characters to the encoder and decoder.' % char)
            if (len(message) - 1) != message.index(char):
                self._previousMessage.morse += ' '

        # Returns the encoded message object
        return self._previousMessage

    @property
    def previousMessage(self):
        return self._previousMessage


class Decoder:
    """
    A set of methods to decode morse code strings into plaintext
    """

    def __init__(self, **kwargs):
        # Define the dot, dash and separator symbols
        try:
            self.dot = kwargs['dot']
        except KeyError:
            self.dot = '.'

        try:
            self.dash = kwargs['dash']
        except KeyError:
            self.dash = '-'

        try:
            self.separator = kwargs['separator']
        except KeyError:
            self.separator = '/'

        # Initialize the previousMessage attribute
        self._previousMessage = Message()

    def decode(self, morse: str):
        # Set the morse value of the previousMessage attribute
        self._previousMessage.morse = morse

        # Split the message into a list with each word as a separate value
        message = morse.split(' %s ' % self.separator)

        # Split each word of the message into individual characters
        for word in range(len(message)):
            message[word] = message[word].split(' ')

        # Decode the message
        for word in message:
            for char in word:
                if char == '':
                    pass
                else:
                    try:
                        self._previousMessage.plaintext += character.characters['morse'][char].plaintext
                    except KeyError:
                        raise ValueError('%s is not defined as a character!  Please wait foe the developer to add the '
                                         'ability to add custom characters to the encoder and decoder.' % char)

            if (len(message) - 1) != message.index(word):
                self._previousMessage.plaintext += ' '

        # Return the decoded message
        return self._previousMessage

    @property
    def previousMessage(self):
        return self._previousMessage


# Simple testing setup
if __name__ == '__main__':
    encoder = Encoder()
    decoder = Decoder()

    encoder.encode('This is morse code.')
    decoder.decode(encoder.previousMessage.morse)

    print('Encoded message:')
    print(encoder.previousMessage.morse)
    print('\nDecoded message:')
    print(decoder.previousMessage.plaintext)
