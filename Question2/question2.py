import os
import binascii

from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

def encrypt(key, plaintext):
    iv = b'\x00' * 16

    encryptor = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
    ).encryptor()

    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    ciphertext = binascii.hexlify(ciphertext).decode()
    return (ciphertext)

def set_length(word, plaintext, ciphertext):
    if len(word) < 17:
        stripped_plaintext = plaintext.rstrip('\n')
        word = word.rstrip('\n')
        new_word = word.ljust(16)
        b = bytes(new_word, 'utf-8')
        new_cipher = plaintext.ljust(32, '\x00')
        b_cipher = bytes(new_cipher, 'utf-8')

        x = encrypt(b, b_cipher)

        if ciphertext in x:
            print(x)
            print(word)

def read_dictionary():
    fp = open("dictionary.txt","r")

    plaintext = input("Enter plaintext here: ")
    plaintext = plaintext[0:16]

    ciphertext = input("Enter ciphertext here: ")
    ciphertext = ciphertext[0:30]

    for x in fp:
        set_length(x, plaintext, ciphertext)

def main():
    read_dictionary()

main();
