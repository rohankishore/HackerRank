#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    for element in arr:
        if element > 0:
            pos_arr.append(element)
        elif element < 0:
            neg_arr.append(element)
        elif element == 0:
            zero_arr.append(element)
            
    # format() to insert trailing zeroes incase if the result is something like "0.5" or "0.8"
            
    neg_ratio = format(round((len(neg_arr)/len(arr)), 6), '6f')
    pos_ratio = format(round((len(pos_arr)/len(arr)), 6), '6f')
    zero_ratio = format(round((len(zero_arr)/len(arr)), 6), '6f')
    
    print(pos_ratio)
    print(neg_ratio)
    print(zero_ratio)

if __name__ == '__main__':
    n = int(input().strip())
    neg_arr = []
    pos_arr = []
    zero_arr = []

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
