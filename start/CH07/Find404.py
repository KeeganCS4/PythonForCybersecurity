#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Keegan 11/2

# import
import os

# get current directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# build file path
file_path = os.path.join(script_dir, "access.log")

# open file for reading
f = open(file_path, "r")

while True:
    line = f.readline()
    if not line:
        break
    if "404" in line:
        if "index.php" in line:
            print(line)

f.close()