# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    x = [0] + stops + [distance]
    n = len(stops)
    count = 0
    currentRefill = 0
    while (currentRefill <=n):
        lastRefill = currentRefill
        while (currentRefill <= n and x[currentRefill+1]-x[lastRefill]<=tank):
            currentRefill = currentRefill +1
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= n:
            count += 1
    return count


d = int(input())
m = int(input())
n = int(input())
stops = list(map(int,input().split(" ")))
print(compute_min_refills(d, m, stops))

