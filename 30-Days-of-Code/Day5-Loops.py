#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (2 <= n <= 20):  #constraint
        for i in range(1, 11):
            res = n*i
            print(n, "x", i, "=", res)
