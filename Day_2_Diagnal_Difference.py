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
    LR_diag = 0
    RL_diag = 0
    i, j = 0, 0
    while(i < len(arr)):
        LR_diag += arr[i][j]
        i+=1
        j+=1
    
    k, l = 0, len(arr)-1
    while(k < len(arr)):
        RL_diag += arr[k][l]
        k+=1
        l-=1
    
    
    
    result = abs(RL_diag - LR_diag)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
