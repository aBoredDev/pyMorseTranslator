# pyMorse

pyMorse provides tools for encoding and decoding strings in
morse code.  A typical usage scenario looks like this:

    #!/usr/bin/env python
    from pyMorse import translator
    
	
    # Initialize the encoder and decoder
    encoder = translator.Encoder()
	decoder = translator.Decoder()
	
	# Encode the message
	print(encoder.encode('This is morse code.').morse)
    
    # Do stuff with the message
	
	# Decode the message
	print(decoder.decode(encoder.previousEncode.morse).plaintext)

The output of this code would be:

    - .... .. ... / .. ... / -- --- .-. ... . / -.-. --- -.. . .-.-.-
    THIS IS MORSE CODE.


## Features

### Current Features

* Morse encoding

* Morse decoding

* Custom symbols for dots, dashes and separators

### Planned Features

1. Custom characters for encoders and decoders

## Resources

Currently the only resource available is the files themselves, available at https://github.com/Eagle-Eye2324/pyMorse