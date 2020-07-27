# Uses python3
import sys

def get_change(m):
    a = [1,2,1,1]
    if m <5:
        return a[m-1]
    else:
        for i in range(4,m):
            a.append(1+min(a[i-1],a[i-3],a[i-4]))
        #return 1+min(get_change(m-1),get_change(m-3),get_change(m-4))
        return a[m-1]
    #write your code here
        


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
