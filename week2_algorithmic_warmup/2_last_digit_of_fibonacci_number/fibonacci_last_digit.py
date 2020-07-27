def calc_fib(n):
    Series = [1]*(n+1)
    Series[0] = 0
    for i in range(2,n+1):
        Series[i] = (Series[i-1]+Series[i-2])%10
    return Series[n]

n = int(input())
print(calc_fib(n))
