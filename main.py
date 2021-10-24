import os

from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)


# def decrypt(key, ciphertext, tag):
#     # Construct a Cipher object, with the key, iv, and additionally the
#     # GCM tag used for authenticating the message.
#     decryptor = Cipher(
#         algorithms.AES(key),
#         modes.GCM(iv, tag),
#     ).decryptor()
#
#     # We put associated_data back in or the tag will fail to verify
#     # when we finalize the decryptor.
#     decryptor.authenticate_additional_data(associated_data)
#
#     # Decryption gets us the authenticated plaintext.
#     # If the tag does not match an InvalidTag exception will be raised.
#     return decryptor.update(ciphertext) + decryptor.finalize()
#
# print(decrypt(
#     key,
#     b"authenticated but not encrypted payload",
#     iv,
#     ciphertext,
#     tag
# ))


def encrypt(key, plaintext):
    # Generate a random 96-bit IV.
    iv = os.urandom(12)


    # Construct an AES-GCM Cipher object with the given key and a
    # randomly generated IV.
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
    ).encryptor()

    # Encrypt the plaintext and get the associated ciphertext.
    # GCM does not require padding.
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return ciphertext

def set_length(word):
    if len(word) < 17:
        new_word = word.ljust(16)
        b = bytes(new_word, 'utf-8')
        print(encrypt(b, b'This is a top secret'))

def read_dictionary():
    fp = open("dictionary.txt","r")
    for x in fp:
        set_length(x)

def main():
    # decrypt("Hello", "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9", "This is a top secret.")
    # print(encrypt(b'Test            ', b'This is a top secret'))
    read_dictionary()

main();
