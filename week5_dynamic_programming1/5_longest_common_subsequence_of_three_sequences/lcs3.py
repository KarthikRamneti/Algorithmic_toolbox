#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    import numpy as np
    n = len(a)
    m = len(b)
    l = len(c)
    D = np.zeros((n+1,m+1,l+1))
    
    for i in range(1,n+1):
        for j in range(1,len(b)+1):
            for k in range(1,l+1):
                if a[i-1] == b[j-1]==c[k-1]:
                    m = D[i-1][j-1][k-1]+1
                else:
                    m = max(D[i-1][j][k],D[i][j-1][k],D[i][j][k-1])
                D[i][j][k] = m
    return int(D[-1][-1][-1])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    l = int(input())
    c = list(map(int, input().split()))
    print(lcs3(a, b, c))
