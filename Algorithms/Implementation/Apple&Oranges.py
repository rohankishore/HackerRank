#!/bin/python3

import math
import os
import random
import re
import sys

# s = sam's house' start x coordinate
# t = sam's house' end x coordinate
# a = apple tree's x coord
# d = distance
# m = no of apples
# n = no of oranges


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_after_addition = [x+a for x in apples]
    orange_after_addition = [y+b for y in oranges]
    apple_nos = []
    orange_nos = []
    
    for element in orange_after_addition:
        if s <= element <= t:
            orange_nos.append(element)
            
    for element in apple_after_addition:
        if s <= element <= t:
            apple_nos.append(element)
    
    print(len(apple_nos))
    print(len(orange_nos))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
