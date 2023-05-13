#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    lenstr = len(arr)
    # print (lenstr)
    for i in range (len(arr)):
        if arr[i] == 0:
            zero =zero +1
        if arr[i] >0:
            positive = positive +1
        if arr[i] < 0:
            negative = negative +1
    pro_positive = positive / lenstr
    pro_negative = negative / lenstr
    pro_zero = zero / lenstr
    print (pro_positive)
    print (pro_negative)
    print (pro_zero)

    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)