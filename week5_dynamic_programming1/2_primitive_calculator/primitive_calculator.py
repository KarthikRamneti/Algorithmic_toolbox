# Uses python3
import sys
import math

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def primitive(n):
    a = [[1],[1,2],[1,3]]
    if n < 4:
        return a[n-1]
    else:
        for i in range(4,n+1):
            b = [n,n,n]
            if i % 3 ==0:
                 b[2]=len(a[i//3 -1])
            if i % 2 ==0:
                 b[1] = len(a[i//2 -1])
            b[0] = len(a[i-1-1])
            m = min(b)
            for j in range(len(b)):
                if b[j] == m:
                    k = j
                    break
            if k == 2:
                s = a[i//3 -1] + [i]
                a.append(s)
            if k == 1:
                s = a[i//2 -1] + [i]
                a.append(s)
            if k == 0:
                s = a[i-1 -1] + [i]
                a.append(s)
        return a[-1]
                 



n = int(input())

sequence = list(primitive(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

#print(primitive(n))
