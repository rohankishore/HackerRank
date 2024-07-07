#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    final_array = []
    alice = 0
    bob = 0

    if a[0] > b[0]:
        alice += 1
    if a[0] < b[0]:
        bob += 1

    if a[1] > b[1]:
        alice += 1
    if a[1] < b[1]:
        bob += 1

    if a[2] > b[2]:
        alice += 1
    if a[2] < b[2]:
        bob += 1

    final_array.append(alice)
    final_array.append(bob)

    return final_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
