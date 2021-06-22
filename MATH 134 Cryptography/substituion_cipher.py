'''
Substitution Cipher
'''
__author__ = 'Simon Lee in Math 134, siaulee@ucsc.edu'

def encode(plaintext, cipher):
    return "".join(cipher.get(character.upper()) or character
                   for character in plaintext)


def decode(secret, encoding_cipher):
    decode_cipher = {value: key for key, value in encoding_cipher.items()}
    return encode(secret, decode_cipher)


def main():
    cipher = {"A": "Q", "B": "C", "C": "X", "D": "G", "E": "B",
              "F": "W", "G": "R", "H": "D", "I": "A", "J": "T",
              "K": "U", "L": "O", "M": "P", "N": "H", "O": "M",
              "P": "J", "Q": "N", "R": "E", "S": "Y", "T": "I",
              "U": "L", "V": "V", "W": "F", "X": "K", "Y": "Z",
              "Z": "S"}

    plaintext = input("enter message: ")
    secret = encode(plaintext, cipher)
    plaintext = decode(secret, cipher)
    print(secret, plaintext)


if __name__ == '__main__':
    main()

