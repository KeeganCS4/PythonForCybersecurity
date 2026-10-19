#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By 10/19

import codecs

# Ask user for message
message = input("Enter a message: ").lower()
# final_message = ""


# 2 line rot13
rot13 = codecs.encode(message, 'rot_13')
print(rot13)

# # ASCII english alphabet is 97 - 122

# # for each letter convert to number -> rotate -> convert back to letter
# for letter in message:
#     # convert letter to number
#     ascii_num = ord(letter)

#     # if its not a special character add 13 otherwise pass it through
#     if(ascii_num < 97 or ascii_num > 122):
#         pass
#     else:
#         ascii_num = ascii_num + 13

#     # simple bypass that doesnt account for all special characters
#     # if ascii_num >= 97:
#     #     ascii_num = ascii_num + 13

#     # if past z, wrap around
#     if ascii_num > 122:
#         ascii_num = ascii_num - 26

#     # convert number to letter 
#     new_letter = chr(ascii_num)

#     # append new letter to newmsg
#     final_message = final_message + new_letter

# # print new message
# print(final_message)