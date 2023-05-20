#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    dau2 = 1
    li = []
    for i in range(0,len(s)-1):
        print ("dòng 1:  " + str(s[i]))
        for j in range (dau2,len(s)):
            print ("dòng 2:  "+ str(s[j]))
            if (s[j] + s[i]) // k != 0:
                li.append(s[j])
                li.append(s[i]) 
                # print ("\n%%%%%%%%")
                # print (s[i])
                # print (s[j])
           
        dau2 = dau2 + 1    
    li.sort()   
    kq = set(li)
    li1 = list (kq)
    kq_end = len(li1)
    print ("\n\n")
    # print (li)
    print (kq_end)
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
