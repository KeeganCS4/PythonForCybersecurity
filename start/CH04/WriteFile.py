#!/usr/bin/env python3
# Sample script that writes to a file
# By Keegan 10/14

# import
import os

# get current directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# build file path
file_path = os.path.join(script_dir, "testfile.txt")

# open file for writing
# f = open("/home/keegan/Downloads/PythonForCybersecurity/start/CH04/testfile.txt", "w") Wrong way, breaks when directories change
f = open(file_path, "w")

# write to the file
f.write("Hello World\n")
f.write("My name is Keegan\n")
f.write("I like rubber ducks\n")

# close file
f.close()