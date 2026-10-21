#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Keegan 10/21

from cryptography.fernet import Fernet
import time

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

# welcome banner
print()
banner = "Welcome to the encryption tool!"
print(banner.center(65))
print("=" * 65)
what_do = ""
save = False
# a while loop that keeps the tool alive until you close with the exit command "c"
while(what_do != "c"):
    # asks user to choose operation
    what_do = input("""What do you want to do? 
    1. Encrypt\t\t(E)
    2. Decrypt\t\t(D)
    3. Generate Key\t(G)
    4. Close Tool\t(C)
    Operation: """).lower()
    what_do = what_do[0]
    time.sleep(1)

    # Key: yJb4bUvbJGzWIXuE-hGEEIbtYhd8utfpSoYfLdQka_8=
    # Encrypted message: AAAAABq2OU9g4C7VrSoVpR7PdM9VG3AfqM6AMfQqltfotX6x9np6noRts0Xxg_gmvaPPwh1mxkRJOq_cBOu1Y-EfF185rizww==

    # if user chooses to create key, calls create key function
    if(what_do == "g"):
        print("\nYou chose Generate Key!\n")
        time.sleep(1)
        key = create_key()
        # tool already knows the key, this automatically applies the key
        save_key = input("Would you like to save key? ").lower()
        save_key = save_key[0]
        if(save_key == "y"):
            save = True
        else:
            print("Key: {key}\n")
        time.sleep(1)
    # if user chooses to encrypt, gathers plain text message and calls encrypt
    elif(what_do == "e"):
        print("\nYou chose Encryption!\n")
        time.sleep(1)
        # get key
        if(save == True):
            pass
        else:
            key = input("Key: ")
        # get message
        message_plain = input("Message: ")
        # assign plain message to cipher_text since you are encrypting
        cipher_text = encrypt(message_plain, key)
        # print out encrypted text
        print(f"Encrypted Message: {cipher_text}\n")
        time.sleep(1)
    # if user chooses to decrypt, gathers encrypted message and calls decrypt
    elif(what_do == "d"):
        # get key
        if(save == True):
            pass
        else:
            key = input("Key: ")
        # get message
        message_encrypt = input("\nMessage: ")
        # assign message to plain_text since you are decrypting
        plain_text = decrypt(message_encrypt, key)
        # print out plain text
        print(f"Decrypted Message: {plain_text}\n")
        time.sleep(1)