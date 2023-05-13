#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    
    for i in range (len(grades)):
        
        if grades[i] < 38:
            continue
        else:
            tmp = grades[i]
            tmp1 = tmp % 5
            if tmp1 ==3:
                tmp = tmp +2
                grades[i] = tmp
            elif tmp1 ==4:
                tmp = tmp+1
                grades[i] = tmp
            else:
                continue
    return grades
                
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
