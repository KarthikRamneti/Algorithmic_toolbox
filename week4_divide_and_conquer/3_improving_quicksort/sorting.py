# Uses python3
import sys
import random

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    ra = j
    k =0
    for index in range(j+1,r+1):
        if a[index] == a[j]:
            ra += 1
            k+=1
            a[ra], a[index] = a[index], a[ra]
    return j , k


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m,ra = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    #randomized_quick_sort(a, m, m +ra);
    randomized_quick_sort(a, m + ra+1, r);
 

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
