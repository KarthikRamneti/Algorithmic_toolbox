# Uses python3
import sys

def fibonacci_sum(n):
    Series = [1]*int(1e6)
    Series[0] = 0
    a = [0,1]
    for i in range(2,n+1):
        Series[i] = (Series[i-1]+Series[i-2])%10
        if Series[i] == 1 and Series[i-1] == 0:
            a.pop(-1)
            break
        a.append(Series[i])
    quotient = n//len(a)
    rem = n%len(a)
    a_total = 0
    for i in range(len(a)):
        a_total += a[i]
    suma = (a_total*quotient)%10
    for i in range(rem+1):
        suma = (suma + a[i])%10
    return suma


def fibonacci_partial_sum(m,n):
    a = fibonacci_sum(n) - fibonacci_sum(m-1)
    return a%10

m, n = map(int, input().split())
print(fibonacci_partial_sum(m, n))
