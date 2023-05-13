#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    run1 = 0
    run2 = 1
    count = 0
    for i in range (run1,len(ar)):
        for j in range (run2, len(ar)):
            run1 = run1 + 1
            # print (ar[i], ar[j])
            if (ar[i] + ar[j]) % k ==0:
                count =count +1
        run2 = run2+ 1
    
    print (count)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    # fptr.write(str(result) + '\n')

    # fptr.close()
