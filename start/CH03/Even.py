#!/usr/bin/env python3
# example working with modulus
#By Keegan 10/7

number = int(input("Enter a number: ")) # ask user for a number
if number % 2 == 0: # check if number is even
    print(f"{number} is even.") # print message if number is even
else:
    print(f"{number} is NOT even.") # print message if number is odd