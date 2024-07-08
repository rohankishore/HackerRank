#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    asc = sorted(arr, reverse=False)
    des = sorted(arr, reverse=True)

    mini_sum = str((sum(asc)) - (asc[4]))
    max_sum = str((sum(des) - des[4]))

    print(mini_sum + " " + max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
