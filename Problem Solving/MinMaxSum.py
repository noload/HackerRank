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
    minSum=0
    maxSum=0
    arr.sort()
    for num in arr[1:]:
        maxSum+=num
    for num in arr[:len(arr)-1]:
        minSum+=num
    print(minSum,end=" ")
    print(maxSum,end="")
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
