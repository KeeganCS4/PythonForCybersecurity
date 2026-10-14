#!/usr/bin/env python3
# Sample script that writes to a file
# By Keegan 10/14


# open file for writing
f = open("testfile.txt", "w")

# write to the file
f.write("Hello World\n")
f.write("My name is Keegan\n")
f.write("I like rubber ducks")

# close file
f.close()