#!/usr/bin/env python3
# Sample script that writes to a file
# By Keegan 10/14

# import
import os

# get current directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# build file path
file_path = os.path.join(script_dir, "hackme.txt")

# open file for writing
# f = open("/home/keegan/Downloads/PythonForCybersecurity/start/CH04/testfile.txt", "w") Wrong way, breaks when directories change
f = open(file_path, "w")

# get user input: name, fav color, first pets name, mothers maiden name, elementary school attend
name = input("What is your name? ")
f_color = input("What is your favorite color? ")
p_name = input("What is your first pets name? ")
m_m_name = input("What is your mothers maiden name? ")
elem_school = input("What was your first elementary school? ")

# write to the file
f.write(f"{name}\n")
f.write(f"{f_color}\n")
f.write(f"{p_name}\n")
f.write(f"{m_m_name}\n")
f.write(f"{elem_school}\n")

# close file
f.close()