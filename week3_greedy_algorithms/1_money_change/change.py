# Uses python3
import sys

def get_change(m):
    count = 0
    while m >0:
        if m -10 >=0:
            count += 1
            m = m -10
        elif m-5>=0:
            count += 1
            m = m -5
        elif m-1 >=0:
            count += 1
            m = m -1
    #write your code here
    return count

m = int(input())
print(get_change(m))
