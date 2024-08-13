#!/bin/python3

import math
import os
import random
import re
import sys


def marcsCakewalk(calorie):
    min_cal = calorie
    min_cal.sort(reverse=True)
    
    n = 0
    sum_list = []
    
    for i in min_cal:
        val = ((2**n)*i)
        sum_list.append(val)
        n += 1
        
    sum_val = sum(sum_list)
    return sum_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
