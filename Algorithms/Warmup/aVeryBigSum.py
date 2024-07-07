#!/bin/python3

# You can use sum() to easily solve this problem.

import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))
    
    result = aVeryBigSum(ar)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
