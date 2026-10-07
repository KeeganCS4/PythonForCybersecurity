#!/usr/bin/env python3
# example workign with conditionals
#By Keegan 10/5

# grade = 93

# if grade >= 95:
#     print("A+")
# elif grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# elif grade >= 60:
#     print("D")
# else:
#     print("F")

# print("\nDone")


# Ask user about their day
good_day = input("Is today a good day? (y/n): ")

if good_day == "y": # if day is good, print a message
    print("Yes it is!")
else:
    print("Sorry to hear that.") # if day is bad, print a different message