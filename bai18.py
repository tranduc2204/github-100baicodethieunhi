#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    tmp = []
    tmp1 = arr.copy()
    sodauver1 = 0
    sodau = arr[sodauver1]

    count = 0
    for i in arr:
        if i == arr[i]:
            count = count + 1 
            if count > 1:
                tmp.append(i)
            else:
                pass
        # sodauver1 = sodauver1 + 1
    print (tmp)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
