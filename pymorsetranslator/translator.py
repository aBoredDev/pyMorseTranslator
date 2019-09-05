#!/usr/bin/env python
from pyMorseTranslator import character


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

    def __init__(self, *args, **kwargs):
        """
        Constructor for the encoder.
            customs: A list or tuple of Character objects
            **kwargs:
                dot='.'
                dash='-'
                separator='/'
        """
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

        # Initialize the custom characters list
        self.customs = {}
        try:
            for char in args[0]:
                self.customs.update({char.plaintext: char})
        except IndexError:
            pass

    def encode(self, plaintext: str):
        """
        Encode a plaintext string into morse code.

        Arguments:
            plaintext: The string to encode.
        """
        # Set the plaintext value of the previousMessage attribute
        self._previousMessage.plaintext = plaintext

        # Split the message into individual characters
        message = list(plaintext.upper())

        for char in message:
            if char in self.customs.keys():
                self._previousMessage.morse += self.customs[char].morse
            else:
                if char == ' ':
                    self._previousMessage.morse += '%s ' % self.separator
                else:
                    try:
                        self._previousMessage.morse += character.characters['plaintext'][char].morse
                    except KeyError:
                        raise ValueError('%s is not defined as a character!  Have yoou added it as a custom character?' % char)
            if (len(message) - 1) != message.index(char):
                self._previousMessage.morse += ' '

        # Replace the default symbols with the symbols defined by the user
        self._previousMessage.morse.replace('.', self.dot)
        self._previousMessage.morse.replace('-', self.dash)
        
        # Returns the encoded message object
        return self._previousMessage

    @property
    def previousMessage(self):
        """
        The last message that has been encoded

        Returns: a Message object
        """
        return self._previousMessage

    def addCustom(self, plaintext, morse):
        """
        Adds a character to the dictionary of custom characters for an encoder object

        Arguments:
            plaintext: The plaintext character to be added.
            morse: The morse code version of the character.
        """
        self.customs.update({plaintext: character.Character(plaintext, morse)})

    def addCustoms(self, customs):
        """
        Adds a list or tuple of characters to the dictionary of custom characters for an encoder object

        Arguments:
            customs: A tuple or list of custom characters to be added.
        """
        for char in customs:
            self.customs.update({char.plaintext: char})

    def listCustoms(self):
        """
        Lists all the custom characters for an encoder

        Returns: List of Character objects
        """
        customs = []
        for key in self.customs.keys():
            customs.append(self.customs[key])
        return customs


class Decoder:
    """
    A set of methods to decode morse code strings into plaintext
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the decoder.
            customs: A list or tuple of Character objects
            **kwargs:
                dot='.'
                dash='-'
                separator='/'
        """
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

        # Initialize the custom characters list
        self.customs = {}
        try:
            for char in args[0]:
                self.customs.update({char.morse: char})
        except IndexError:
            pass

    def decode(self, morse: str):
        """
        Decode a morse-encoded string into plaintext.

        Arguments:
            morse: The string to decode
        """
        # Set the morse value of the previousMessage attribute
        self._previousMessage.morse = morse

        # Replace the user-defined symbols with the default ones
        morse.replace(self.dot, '.')
        morse.replace(self.dash, '-')
        morse.replace(self.separator, '/')

        # Split the message into a list with each word as a separate value
        message = morse.split(' %s ' % self.separator)

        # Split each word of the message into individual characters
        for word in range(len(message)):
            message[word] = message[word].split(' ')

        # Decode the message
        for word in message:
            for char in word:
                if char in self.customs.keys():
                    self._previousMessage.plaintext += self.customs[char].plaintext
                else:
                    if char == '':
                        pass
                    else:
                        try:
                            self._previousMessage.plaintext += character.characters['morse'][char].plaintext
                        except KeyError:
                            raise ValueError('%s is not defined as a character!  Have you added it as a custom character?' % char)

            if (len(message) - 1) != message.index(word):
                self._previousMessage.plaintext += ' '

        # Return the decoded message
        return self._previousMessage

    @property
    def previousMessage(self):
        """
        The last message that has been decoded

        Returns: a Message object
        """
        return self._previousMessage

    def addCustom(self, plaintext, morse):
        """
        Adds a character to the dictionary of custom characters for a decoder object

        Arguments:
            plaintext: The plaintext character to be added.
            morse: The morse code version of the character.
        """
        self.customs.update({morse: character.Character(plaintext, morse)})

    def addCustoms(self, customs):
        """
        Adds a list or tuple of characters to the dictionary of custom characters for a decoder object

        Arguments:
            customs: A tuple or list of custom characters to be added.
        """
        for char in customs:
            self.customs.update({char.morse: char})

    def listCustoms(self):
        """
        Lists all the custom characters for a decoder

        Returns: List of Character objects
        """
        customs = []
        for key in self.customs.keys():
            customs.append(self.customs[key])
        return customs


# Simple testing setup
if __name__ == '__main__':
    customs = [
        character.Character('@', '.--.-.'),
        character.Character(':', '---..-'),
        character.Character('=', '-...-')
    ]
    
    encoder = Encoder(customs)
    decoder = Decoder(encoder.listCustoms())

    encoder.encode('This is morse code.')
    decoder.decode(encoder.previousMessage.morse)

    print('Encoded message:')
    print(encoder.previousMessage.morse)
    print('\nDecoded message:')
    print(decoder.previousMessage.plaintext)
