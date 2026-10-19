#!/usr/bin/env python3
# ASCII generator
# Uses chr() to create ASCII characters
# By Keegan 10/19

# loop 0-127
for i in range(128):
    # print number, print chr(number)
    print(f"{i}\t'{chr(i)}'")
