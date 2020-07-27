# Uses python3
from sys import stdin

def get_fibonacci_huge(n):
    Series = [1]*int(1e6)
    Series[0] = 0
    a = [0,1]
    for i in range(2,n+1):
        Series[i] = (Series[i-1]+Series[i-2])%10
        if Series[i] == 1 and Series[i-1] == 0:
            a.pop(-1)
            break
        a.append(Series[i])
    rem = n%len(a)
    return a[rem]


def fibonacci_sum_squares(n):
    a = get_fibonacci_huge(n)*get_fibonacci_huge(n+1) 
    return a %10

n = int(input())
print(fibonacci_sum_squares(n))
