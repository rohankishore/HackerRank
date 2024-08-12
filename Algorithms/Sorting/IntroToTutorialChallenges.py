#!/bin/python3

import os

def introTutorial(V, arr):
    ind = 0
    for i in arr:
        if i == V:
            ind = arr.index(V)
    return ind
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
