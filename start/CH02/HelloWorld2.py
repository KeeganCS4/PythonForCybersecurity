#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created 9/28 by Keegan

# Suggestion, build out 1 line at a time
# Once multiple print statemetns exist, put a breakpoint at first print line
# Then walk through as an example of "debugging"

print("Hello World!")
# say hello to the world

user_name = input("What is your name? ")
# get user name

print("Hello " + user_name + "!")
# say hello to user

user_age = int(input("How old are you? "))
age = user_age + 2
print("You will be " + str(age) + " in 2 years!")
# calculate user age