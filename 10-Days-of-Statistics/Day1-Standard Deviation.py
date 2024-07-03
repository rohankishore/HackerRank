#!/bin/python3

import math
import os
import random
import re
import sys


def stdDev(arr):
    sum_of_arr = sum(arr)
    mean = sum_of_arr/len(arr)
    
    new_list = [] # list where the elements after subtraction will be added
    
    for i in arr:
        elem_after_diff = (i - mean)**2 #
        new_list.append(elem_after_diff)
    
    sum_after_diff = sum(new_list) # sum of elements after "elem_after_diff" operation
    variance = sum_after_diff/len(arr)
    std_dev = math.sqrt(variance) # standard deviation is the sqrt of variance
    std_dev = round(std_dev, 1)
    return std_dev
    
    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    print(stdDev(vals))
