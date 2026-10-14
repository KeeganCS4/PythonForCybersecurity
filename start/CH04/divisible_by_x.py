#!/usr/bin/env python3
# Sample script that checks if a number is divisible by another number
# By Keegan 10/14

# math function
def divisible(numb1, numb2):
    check = numb1 % numb2
    if(check == 0):
        print(f"{numb1} is divisible by {numb2}\n")
    else:
        print(f"{numb1} is NOT divisible by {numb2}\n")


for i in range(2):
    numb1 = int(input("What is the number: "))
    numb2 = int(input("What is the divisor: "))
    divisible(numb1, numb2)
    
