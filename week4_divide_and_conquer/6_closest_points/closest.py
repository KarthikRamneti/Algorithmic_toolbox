#Uses python3
import sys
import math

def t2(x):
    return x[1]

def minimum_distance(List,l,r):
    #write your code here
    if r-l<=1:
        d = ((List[l][0]-List[r][0])**2+(List[l][1]-List[r][1])**2)**0.5
        return d
    
    m = (l+r)//2
    d1 = minimum_distance(List,l,m)
    d2 = minimum_distance(List,m,r)
    d = min(d1,d2)
        
    X = []
    for i in range(l,r+1):
        if List[m][0]-d<=List[i][0]<=List[m][0]+d:
            X.append(List[i])
    
    X.sort(key = t2)
    for i in range(len(X)):
        for j in range(1,7):
            if (i+j) < len(X):
                dist = ((X[i][0]-X[i+j][0])**2+(X[i][1]-X[i+j][1])**2)**0.5
                d = min(d,dist)
    return d

if __name__ == '__main__':
    n = int(input())
    List = []
    for i in range(n):
        p = list(map(int, input().split()))
        List.append(p)
    List.sort()
    print("{0:.9f}".format(minimum_distance(List,0,n-1)))
