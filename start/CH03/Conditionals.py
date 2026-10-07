#!/usr/bin/env python3
# example workign with conditionals
#By Keegan 10/5

# Ask user about their day
# good_day = input("Is today a good day? (y/n): ")

# if good_day.lower() == "y" or good_day.lower() == "yes": # if day is good, print a message
#     for i in range(10): # loop 10 times
#         print("Yes it is!")
# elif good_day.lower() == "n" or good_day.lower() == "no": # if day is bad, print a different message
#     for i in range(10): # loop 10 times
#         print("Sorry to hear that.")
# else: # if user input is not recognized, print a message
#     for i in range(10): # loop 10 times
#         print("It's a yes or no question.")


number = int(input("Enter a number: ")) # ask user for a number
if number % 2 == 0: # check if number is even
    print(f"{number} is even.") # print message if number is even
else:
    print(f"{number} is NOT even.") # print message if number is odd