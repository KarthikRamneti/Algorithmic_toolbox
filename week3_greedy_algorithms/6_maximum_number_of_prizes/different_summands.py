# Uses python3
import sys
import math

def optimal_summands(n):
    a = int((math.sqrt(1+8*n)-1)/2)
    summands = []
    count = 0
    for i in range(1,a):
        count += i
        summands.append(i)
    summands.append(n-count)
    return summands


n = int(input())
summands = optimal_summands(n)
print(len(summands))
for x in summands:
    print(x, end=' ')
