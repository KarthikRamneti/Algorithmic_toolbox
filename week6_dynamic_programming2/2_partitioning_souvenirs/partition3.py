# Uses python3
import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        #print(c)
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1
    return 0

def withoutRepeat(W,w):
    import numpy as np
    M = np.zeros((len(w)+1,W+1))
    for i in range(1,len(w)+1):
        for j in range(W+1):
            M[i][j] = M[i-1][j]
            if w[i-1]<=j:
                val = M[i-1][j-w[i-1]]+w[i-1]
                if val <= W and val > M[i][j]:
                    M[i][j] = val
    return M

def partitioning(A):
    suma = sum(A)
    if suma % 3 != 0:
        return 0
    W= suma // 3
    #print(W)
    M = withoutRepeat(W,A)
    #print(M)
    count = 0
    for i in range(len(A)+1):
        if M[i][-1]==W:
            count += 1
    #print(count)
    if count >= 3:
        return 1
    else:
        return 0
    

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    print(partitioning(A))

