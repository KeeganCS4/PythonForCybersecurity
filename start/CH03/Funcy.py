#!/usr/bin/env python3
# example workign with Functions
#By Keegan 8/14

def rick_roll():
    print("Never gonnag ive you up.")
    print("Never gonna let you down.")
    print("Never gonna run around.")
    print("And hurt you.")

def add_two_nums(num1, num2):
    answer = num1 + num2
    print(answer)

def mult_two_nums(num1, num2):
    answer = num1 * num2
    print(answer)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# num1 = 5
# num2 = 7

add_two_nums(num1, num2)
print()
mult_two_nums(num1, num2)
# rick_roll()
# print("Were no strangers to love.......")
# rick_roll()