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
    pos = 0
    neg = 0
    zer = 0
    tot = 0
    for i in arr:
        if(i == 0):
            zer+=1
        elif(i < 0):
            neg+=1
        elif(i > 0):
            pos+=1
        tot += 1
    zer_ratio = zer/tot
    neg_ratio = neg/tot
    pos_ratio = pos/tot
    
    print(round(pos_ratio, 6))
    print(round(neg_ratio, 6))
    print(round(zer_ratio, 6))

        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
