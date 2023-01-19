#!/bin/python3

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
    minSum = 0
    maxSum = 0
    arrMin = []
    arrMax = []
    arr.sort()
    
    arrMin = arr[0:4]
    arrMax = arr[1:5]
    
            
    
    for x in arrMin:
        minSum += x
        
    for y in arrMax:
        maxSum += y
        
    print(minSum, maxSum)
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
