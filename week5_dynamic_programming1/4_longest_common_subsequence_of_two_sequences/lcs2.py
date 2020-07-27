#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    n = len(a)
    m = len(b)
    D= []
    D.append([0]*(n+1))
    for i in range(1,m+1):
        D.append([0]*(n+1))
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[j-1] == b[i-1]:
                m = D[i-1][j-1]+1
            else:
                m = max(D[i-1][j],D[i][j-1])
            D[i][j] = m
    return D[-1][-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    print(lcs2(a, b))

    
