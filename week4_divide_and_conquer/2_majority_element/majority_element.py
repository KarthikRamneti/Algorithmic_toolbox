# Uses python3
import sys

def get_majority_element(a):
    m = int((len(a))/2)
    a = sorted(a)
    for i in range(len(a)-m):
        if a[i] == a[i+m]:
            return i
    #write your code here
    return -1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
