# Uses python3
def edit_distance(s, t):
    #write your code here
    n = len(s)
    m = len(t)
    D= []
    D.append(list(range(n+1)))
    for i in range(1,m+1):
        D.append([i]+[0]*n)
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            m = min(D[i-1][j]+1,D[i][j-1]+1)
            if s[j-1] == t[i-1]:
                m = min(m,D[i-1][j-1])
            else:
                m = min(m,D[i-1][j-1]+1)
            D[i][j] = m
    #print(D)
    
    return D[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
