#!/bin/python3

import math
import os
import random
import re
import sys

# use math.factorial() or use the math formula

def factorial(n):
    if n <= 1 and n >=0:
        return 1
    else:
        return int(math.factorial(n))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
