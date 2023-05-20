#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    diem_A = 0
    diem_B =0
    li = []
    for i in range (len(a)):
        if a[i] > b [i]:
            diem_A = diem_A + 1
        elif a[i] < b [i]:
            diem_B = diem_B + 1
    li.append(diem_A)
    li.append(diem_B)
    print (li)

if __name__ == '__main__':


    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

