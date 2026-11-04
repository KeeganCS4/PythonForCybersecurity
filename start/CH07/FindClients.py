#!/usr/bin/env python3
# Script that scans web server logs for status codes
# Use RegEx to find and report on most frequent status messages
# By Keegan 11/4

# imports
import os
import re
# open log file
# get current directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# build file path
file_path = os.path.join(script_dir, "access.log")

# open file for reading
f = open(file_path, "r")
log_lines = f.readlines()

# setup regex pattern for ips
search_ips = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s"

# dictionary
results_dict = {}

# loop through each line
for line in log_lines:
    # search for pattern
    m = re.search(search_ips, line)
    if m:
        #print(m.group(1))
        # put into dictionary
        result = m.group(1)
        if result in results_dict.keys():
            results_dict[result] += 1
        else:
            results_dict[result] = 1


# sort keys
sorted_keys = sorted(results_dict, key=results_dict.get, reverse = False)
# print dictionary & sort by frequency
for key in sorted_keys:
    print(f"{key}\t {results_dict[key]}")