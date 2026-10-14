#!/usr/bin/env python3
# Sample script that reads a file
# By Keegan 10/14

# import
import os

# get current directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# build file path
file_path = os.path.join(script_dir, "hackme.txt")

# open file for reading
f = open(file_path, "r")

# read contents
contents = f.read()
print(contents)

# close
f.close