#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    tallest = max(candles)
    occurences = candles.count(tallest)
    return occurences

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
