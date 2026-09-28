#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created 

def doMath(numb1, numb2):
    match action:
        case "+":
            result = addition(numb1, numb2)
            print("Answer: " + result)
        case "-":
            result = subtraction(numb1, numb2)
            print("Answer: " + result)
        case "*":
            result = multiplication(numb1, numb2)
            print("Answer: " + result)
        case "/":
            result = division(numb1, numb2)
            print("Answer: " + result)
        case _:
            print("invalid input")
# case ladder do call the operations rather than doing a bunch if statements

def addition(numb1, numb2):
    return numb1 + numb2
# addition function

def subtraction(numb1, numb2):
    return numb1 - numb2
# subtraction function

def multiplication(numb1, numb2):
    return numb1 * numb2
# multiplication function

def division(numb1, numb2):
    return numb1 / numb2
# division function

# action = input("What action would you like? \n1. addition\n2. subtraction\n3. multiplication\n4. division\n")
numbers = input("Enter equation: ")
# user input

parts = numbers.split()
# splits user input into a list
numb1 = float(parts[0])
# turns the first element in list to first number (float)
action = parts[1]
# turns the second item in the list into the action for the cases
numb2 = float(parts[2])
# turns the third item in the list into the second number (float)

doMath(numb1, numb2)
# call of the main function