import os
import binascii

from cryptography.hazmat.backends.openssl.backend import backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

def encrypt(key, plaintext):
    iv = b'\x00' * 16

    encryptor = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend
    ).encryptor()

    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    ciphertext = binascii.hexlify(ciphertext).decode()
    return (ciphertext)

def set_length(word, plaintext, ciphertext):
    if len(word) < 17:
        stripped_plaintext = plaintext.rstrip('\n')
        word = word.rstrip('\n')
        new_word = word.ljust(16)
        b = bytes(new_word)
        new_cipher = plaintext.ljust(32, '\x00')
        b_cipher = bytes(new_cipher)

        x = encrypt(b, b_cipher)

        if ciphertext in x:
            print(x)
            print(word)

def read_dictionary():
    fp = open("dictionary.txt","r")

    plaintext = raw_input("Enter plaintext here: ")
    plaintext = plaintext[0:16]

    ciphertext = raw_input("Enter ciphertext here: ")
    ciphertext = ciphertext[0:32]

    for x in fp:
        set_length(x, plaintext, ciphertext)

def main():
    read_dictionary()

main();
