#Uses python3

import sys

def isTrue(a,b):
    x1 = int(str(a)+str(b))
    x2 = int(str(b)+str(a))
    if x1 > x2:
        return True
    else:
        return False

def largest_number(a):
    #write your code here
    
    res = ""
    while a != []:
        maxNumber = 0 
        for number in a:
            if isTrue(number,maxNumber):
                maxNumber = number
        res += str(maxNumber)
        a.remove(maxNumber)
    return res

data = int(input())
a = list(map(int, input().split(" ")))
print(largest_number(a))
    
