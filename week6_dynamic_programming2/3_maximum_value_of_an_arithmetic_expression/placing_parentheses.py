# Uses python3
import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(s):
    #write your code here
    import numpy as np
    d = []
    O = []
    for i in range(len(s)):
        if i%2 == 0:
            d.append(int(s[i]))
        else:
            O.append(s[i])
    n = len(d)
    m = np.zeros((len(d),len(d)))
    M = np.zeros((len(d),len(d)))
    for i in range(len(d)):
        m[i][i] = M[i][i] = d[i]

    for s in range(1,len(d)):
        for i in range(0,n-s):
            j = i + s
            high = -math.inf
            low = math.inf
            for k in range(i,j):
                a = evalt(M[i][k],M[k+1][j],O[k])
                b = evalt(M[i][k],m[k+1][j],O[k])
                c = evalt(m[i][k],M[k+1][j],O[k])
                d = evalt(m[i][k],m[k+1][j],O[k])
                low = min(low,a,b,c,d)
                high = max(high,a,b,c,d)
            M[i][j] = high
            m[i][j] = low
    return int(M[0][-1])


if __name__ == "__main__":
    print(get_maximum_value(input()))
