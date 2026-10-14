#!/usr/bin/env python3
# Sample script that checks if a number is divisible by another number
# By Keegan 10/14

# math function
def is_divisible(number, divisor):
    check = number % divisor # checking for remainder
    if(check == 0):
        return True # if there is no remainder returns True
    else:
        return False # if there is a remainder returns False

for i in range(2): # a loop to show both expected outputs
    number = int(input("What is the number: ")) # gathers number
    divisor = int(input("What is the divisor: ")) # gathers divisor

    if(is_divisible(number, divisor) == True):
        print(f"{number} is divisible by {divisor}\n") # prints is divisible
    else:
        print(f"{number} is NOT divisible by {divisor}\n") # prints is not divisible
