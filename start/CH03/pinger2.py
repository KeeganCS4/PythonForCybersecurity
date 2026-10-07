#!/usr/bin/env python3
# Second example of pinging from Python
# By Keegan 10/7

import os

#set IP address
ip_prefix = "192.168.0."

for final_octet in range(10):
    #set IP address
    adress = ip_prefix + str(final_octet + 1)

    #build ping CMD
    ping_cmd = f"ping -c 1 -w 1 {adress} > /dev/null 2>&1"

    #run ping
    status_code = os.system(ping_cmd)

    #printstatus
    if status_code == 0:
        print(f"{adress} is ONLINE")
    else:
        print(f"{adress} is offline")