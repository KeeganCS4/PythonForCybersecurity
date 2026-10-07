#!/usr/bin/env python3
# example workign with conditionals
#By Keegan 10/5 Edited 10/7

# Ask user about their day
good_day = input("Is today a good day? (y/n): ")

if good_day.lower() == "y" or good_day.lower() == "yes": # if day is good, print a message
    print("Yes it is!")
elif good_day.lower() == "n" or good_day.lower() == "no": # if day is bad, print a different message
    print("Sorry to hear that.")
else: # if user input is not recognized, print a message
    print("It's a yes or no question.")