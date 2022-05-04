#program to find the maximum element in list without using inbuilt function
'''
ls=[3, 5, 6, 7, 8]
i=0
for [i] in ls:
    if i>i+1:
        pass
    else:
        temp=i
        i=i+1
        i+1=temp
print(ls)
'''
import math
#arbitary argument
def addition(t, *numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum, t, type(numbers)
print(addition(9,3,4,5))

#keyword arguments kwargs
#write a function to calculate sum of first n numbers
#using simple for loop
def sum_num(n):
    sum=0
    for i in range(n+1):
        sum +=i
    return sum
print(sum_num(3))

#another approach

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
    p, n, z= 0, 0, 0
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            n+=1
        else:
            z+=1
    l=len(arr)
    #p=p/l
    #n=n/l
    #z=z/l
    print('%.6f'%(p/l))
    print('negative ratio: %.6f'%(n/l))
    print('zeros ratio: %.6f'%(z/l))
'''if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus([4, 5, 1, 1, -1, -1, 0])
'''
plusMinus([4, 5, 1, 1, -1, -1, 0])


def plusMinus(arr):
    p, n, z= 0, 0, 0
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            n+=1
        else:
            z+=1
    l=len(arr)
    print('%.6f'%(p/l))
    print('%.6f'%(n/l))
    print('%.6f'%(z/l))
    return p, n ,z
'''
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)

#minmax problem
def miniMaxSum(arr):
    arr.sort()
    min, max= 0, 0
    for i in range(1,5):
        #print(arr[i])
        min+=arr[i-1]
        max+=arr[i]
    print(min, max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
'''
def timeConversion(s):
    x=s.split(':')
    print(x)
timeConversion('07:45:00PM')
