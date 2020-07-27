# Uses python3
import sys

def binary_search(a,x):
    l = 0
    r = len(a)-1
    while r>=l:
        b = int((l+r)/2)
        
        if a[b] == x:
            return b
        elif x < a[b]:
            r = b -1
        elif x > a[b]:
            l = b+1
    return -1
        
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1
"""
a = [1,5,8,12,13]
x = [8,1,23,1,11]
print(linear_search(a, 2))
print(binary_search(a, 2))

"""
if __name__ == '__main__':
    data = list(map(int, input().split()))
    a = data[1:]
    x = list(map(int, input().split()))
    for i in x[1:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, i), end = ' ')

