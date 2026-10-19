#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By 10/19


# Ask user for message
message = input("Enter a message: ")
encrypt = input("Encrypt or Decrypt? (e/d): ")
rotate = int(input("Number of rotations:  "))
newmsg = ""

if encrypt == "e":
    # for eacher letter
    for letter in message:
        # Change letter to number, add {rotate}, change message back to text
        letter = ord(letter) + rotate
        # append new letter to newmsg
        newmsg += chr(letter)
    # print new message
    print(newmsg)
else: 
    # for eacher letter
    for letter in message:
        # Change letter to number, remove {rotate}, change message back to text
        letter = ord(letter) - rotate
        # append new letter to newmsg
        newmsg += chr(letter)
    # print new message
    print(newmsg)   