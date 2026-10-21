#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Keegan 10/21

from cryptography.fernet import Fernet

# create key function
def create_key():
    key = Fernet.generate_key()
    key = key.decode()
    return key # yJb4bUvbJGzWIXuE-hGEEIbtYhd8utfpSoYfLdQka_8=

# use key to encrypt
def encrypt(message_plain, key): # Hello World
    # fernet expects a bytes object
    key = key.encode()
    # convert plain text to a bytes object
    message_plain = message_plain.encode()
    # assign the key to the variable f
    key = Fernet(key)
    # encrypt the message with the key
    cipher_text = key.encrypt(message_plain)
    # turn encoded message back to a string
    cipher_text = cipher_text.decode()
    return cipher_text # gAAAAABq2OU9g4C7VrSoVpR7PdM9VG3AfqM6AMfQqltfotX6x9np6noRts0Xxg_gmvaPPwh1mxkRJOq_cBOu1Y-EfF185rizww==

# use key to decrypt
def decrypt(message_encrypt, key):
    # fernet expects a bytes object
    key = key.encode()
    # convert plain text to a bytes object
    message_encrypt = message_encrypt.encode()
    # assign the key to the variable f
    key = Fernet(key)
    # decrypt the message with the key
    plain_text = key.decrypt(message_encrypt)
    # turn the decoded message back into a string
    plain_text = plain_text.decode()
    return plain_text # Hello World

# asks user to choose operation
what_do = input("What do you want to do, Encrypt/Decrypt/Key (E/D/K) ").lower()
what_do = what_do[0]

# Key: yJb4bUvbJGzWIXuE-hGEEIbtYhd8utfpSoYfLdQka_8=
# Encrypted message: AAAAABq2OU9g4C7VrSoVpR7PdM9VG3AfqM6AMfQqltfotX6x9np6noRts0Xxg_gmvaPPwh1mxkRJOq_cBOu1Y-EfF185rizww==

# if user chooses to create key, calls create key function
if(what_do == "k"):
    key = create_key()
    print(key)
# if user chooses to encrypt, gathers plain text message and calls encrypt
elif(what_do == "e"):
    # get key
    key = input("Key: ")
    # get message
    message_plain = input("Message: ")
    # assign plain message to cipher_text since you are encrypting
    cipher_text = encrypt(message_plain, key)
    # print out encrypted text
    print(cipher_text)
# if user chooses to decrypt, gathers encrypted message and calls decrypt
elif(what_do == "k"):
    # get key
    key = input("Key: ")
    # get message
    message_encrypt = input("Message: ")
    # assign message to plain_text since you are decrypting
    plain_text = decrypt(message_encrypt, key)
    # print out plain text
    print(plain_text)
# if user inputs something incorrect
else:
    print("Invalid input")