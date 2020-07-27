# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    w.sort(reverse= True)
    result = 0
    for x in w:
        if x <= W:
            result = result + x
            W = W-x
    return result


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
    return int(M[-1][-1])

if __name__ == '__main__':
    W, n = list(map(int, input().split()))
    w = list(map(int, input().split()))
    print(withoutRepeat(W, w))
