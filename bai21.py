#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    kqcheongang = 0
    kqcheodoc = 0
    bienchay = 0
    bienchaydoc = len(arr) -1
   
    for i in range (len (arr)):
        tmp = arr[i]
        for i in range (len(tmp)):
            kqcheongang = kqcheongang + tmp[bienchay]
            kqcheodoc = kqcheodoc + tmp[bienchaydoc]
            # print (tmp[bienchaydoc])
            bienchay = bienchay + 1
            bienchaydoc = bienchaydoc - 1
            break 
    print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
    print (kqcheongang)
    print (kqcheodoc)
    print (abs (kqcheodoc - kqcheongang))
    
        # kqcheongang = kqcheongang + tmp 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
