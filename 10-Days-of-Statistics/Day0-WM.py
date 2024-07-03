#!/bin/python3

import math
import os
import random
import re
import sys
import array

def weightedMean(X, W):
    X_into_W = [a*b for a , b in zip(X, W)]
    sum_X_into_W = sum(X_into_W)
    sum_W = sum(W)
    weighted_mean = sum_X_into_W/sum_W
    weighted_mean = round(weighted_mean, 1)
    return weighted_mean

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    print(weightedMean(vals, weights))
