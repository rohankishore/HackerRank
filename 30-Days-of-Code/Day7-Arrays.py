#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(str, input().rstrip().split()))
    arr.reverse() #reversing the list
    
    res = str(arr[0]) #initialize with the first element of the list
    
    for i in arr[1:]: # remove first element from the list since we already included it in "res" (line 17)
        res = res + " " + i
    
    print(res)
  
