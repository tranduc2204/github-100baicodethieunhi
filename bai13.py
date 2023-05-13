
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    kqmin = 0
    kqmax = 0
    arr.sort()
    sau = 0
    truoc = 4
    for i in range(sau,truoc):
        kqmin = kqmin +arr[i]
    for i in range(sau+1,truoc+1):
        kqmax = kqmax +arr[i]
    print(kqmin, kqmax)
    print(kqmax)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
