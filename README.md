# xsacks
A crossed substitution alphabetical cipher with secured key

# The sources

Please note that the python implementation is still WiP (actually it works but miss some checks and features)

You can import the xsacks.py module and use xsacks.cipher(msg, key, securekey) and xsacks.decipher(msg, key, securekey).

If you modify xsacks.py, you can run a cipher-decipher test directly from the module, so to be sure you didn't screw things up.
### X-SACKS Cipher Documentation

#### Overview

The X-SACKS cipher is a crossed substitution alphabetical cipher that incorporates a secured key for enhanced security. This cipher combines the principles of crossed substitution and simple substitution to encrypt and decrypt messages.

#### Key Generation

- **Randomization**: Generate a random key for each encryption session to ensure maximum security.
- **Key Length**: Use a longer key to make it more difficult to crack.

#### Encryption and Decryption

1. **Message Preparation**:
   - Split the message into individual letters.
   - Assign a numerical value to each letter based on a chosen alphabet (e.g., ASCII values).

2. **Key Preparation**:
   - Split the key into two parts.
   - Assign numerical values to each letter of the key.

3. **Crossed Substitution**:
   - Add the first value of the message to the first value of the first part of the key.
   - Add the second value of the message to the first value of the second part of the key.
   - Continue this pattern, restarting from the beginning of the key if necessary.

4. **Reconversion**:
   - Convert the resulting numerical values back to letters.

#### Secure Key Encoding

1. **Secure Key Preparation**:
   - Assign numerical values to each letter of the secure key.

2. **Simple Substitution**:
   - Add the numerical values of the key to the numerical values of the secure key.
   - Convert the resulting values back to letters.

#### Example

- **Message**: "Attack now"
- **Key**: "secret"
- **Secure Key**: "cryp"

### Usage

To use the X-SACKS cipher, follow these steps:

1. Generate a random key and secure key.
2. Prepare the message and keys as described above.
3. Perform the crossed substitution and reconversion to encrypt the message.
4. Encode the key using the secure key.
5. Share the encrypted message and encoded key.

To decrypt the message, the recipient needs the encrypted message, the encoded key, and the secure key.

### Security Considerations

- **Key Security**: Ensure the secure key is kept confidential to prevent unauthorized decryption.
- **Key Length**: Use longer keys to increase the difficulty of cracking the cipher.
- **Randomization**: Generate random keys for each encryption session to prevent pattern detection.

### Limitations

- **Complexity**: The X-SACKS cipher can be computationally intensive for large messages.
- **Key Management**: Managing and securely storing the secure key is crucial for the cipher's effectiveness.

### Test

`git clone https://github.com/tcsenpai/xsacks`
`cd xsacks`
`python main.py`

Also play around with main.py for examples.