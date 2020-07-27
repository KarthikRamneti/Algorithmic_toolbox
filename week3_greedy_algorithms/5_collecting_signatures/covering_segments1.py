# Uses python3
import sys

def disjoint(a,b):
    x = max(a[0],b[0])
    y = min(a[1],b[1])
    if x > y:
        return True
    return False

print(disjoint([4,7],[5,6]))
