# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    Series = [1]*int(1e6)
    Series[0] = 0
    a = [0,1]
    for i in range(2,n+1):
        Series[i] = (Series[i-1]+Series[i-2])%m
        if Series[i] == 1 and Series[i-1] == 0:
            a.pop(-1)
            break
        a.append(Series[i])
    rem = n%len(a)
    return a[rem]


n, m = map(int, input().split())
print(get_fibonacci_huge_naive(n, m))
