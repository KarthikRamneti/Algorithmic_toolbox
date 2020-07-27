#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    n = len(a)
    while n>0:
        a1 = max(a)
        b1 = max(b)
        res += a1*b1
        a.remove(a1)
        b.remove(b1)
        n = n-1
    return res

n = int(input())
a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
print(max_dot_product(a, b))
    
