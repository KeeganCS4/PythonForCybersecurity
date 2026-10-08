#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created 9/28 by Keegan
# Updated on 9/30 by Keegan

print("Hello World!\n")
user_name = input("What is your name? ")

# string formatting and concatenation
print("Hello " + user_name)

# string formatting and f-string
print("Hello {0}".format(user_name))
print(f"Hello {user_name}")

# multiple print statements
print("Hello",user_name)

# Constructing variables
message = "Hello " + user_name
print(message)

# removing newline
print("Hello ", end = "")
print(user_name, "")

# old style
print("Hello %s" % user_name)

# Joining text
print(" ".join(["Hello",user_name]))

# just need to force a sync so i can get everything working