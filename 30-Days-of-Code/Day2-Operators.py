#!/bin/python3

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    tip_amount = ((meal_cost/100)*tip_percent)
    tax_amount = ((meal_cost/100)*tax_percent)
    final_amount = meal_cost + tip_amount + tax_amount
    final_amount = round(final_amount)
    print(final_amount)

    

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
