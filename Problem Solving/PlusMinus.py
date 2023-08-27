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
    plus=0
    minus=0
    zeroValue=0
    
    # Write your code here
    for num in arr:
        if(num>0):
            plus+=1
        elif(num<0):
            minus+=1
        elif num==0:
            zeroValue+=1

    plusValue="{:.6f}".format(plus/len(arr))
    minusvalue="{:.6f}".format(minus/len(arr))
    zero="{:.6f}".format(zeroValue/len(arr))
    print(plusValue)
    print(minusvalue)
    print(zero)
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)