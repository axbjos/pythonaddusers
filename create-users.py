#!/usr/bin/python3

''' Add Users Program

    Author: Joe Axberg
    Create Date: 10/7/2022
    Last Modified: 10/7/2022
    
    Description: reads the input file line by line
    and adds the user to the system...blah
'''

import os
import sys
import re

print("Processing Users...")


# processing the file by a linux redirect
#  ./create-users.py < create-users.input
# each line of the file is processed in this loop
for line in sys.stdin:
    print(line)
