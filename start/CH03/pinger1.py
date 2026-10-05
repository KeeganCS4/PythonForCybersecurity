#!/usr/bin/env python3
# First example of pinging from Python
# By Keegan, 10/5

import os

# set IP address
address = "192.168.0.250"

# build ping CMD
ping_cmd = f"ping -c 1 -w 1 {address} > /dev/null 2>&1"

# run ping
status_code = os.system(ping_cmd)

# print status
if status_code == 0:
    print("ONLINE")
else:
    print("Something went wrong")