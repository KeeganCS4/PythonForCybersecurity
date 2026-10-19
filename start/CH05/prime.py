#!/usr/bin/env python3
# prime number checker
# By Keegan 10/19

# loop to show multiple prompts (5, 12, 104743)
def is_prime(number):
    # makes sure number isnt 1
    if number > 1:
        # goes through all numbers up to {number}
        for i in range(2, number):
            # checks if {i} or the numbers up to {number} divide cleanly
            if(number % i) == 0:
                # if its not prime returns False
                return False
            else:
                # if its prime returns True
                return True

# run script 3 times to check all prompts
for i in range(3):
    # ask user for a number
    number = int(input("Enter a number: "))
    if(is_prime(number) == True):
        print(f"{number} is prime.\n")
    else:
        print(f"{number} is NOT prime.\n")