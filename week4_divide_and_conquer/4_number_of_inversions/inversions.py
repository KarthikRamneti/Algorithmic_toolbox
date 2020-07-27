# Uses python3
import sys


def merge(left, right):
    i, j, inversion_counter = 0, 0, 0
    f = list()
    while i < len(left) and j< len(right):
        if left[i] <= right[j]:
            f.append(left[i])
            i += 1
        else:
            f.append(right[j])
            inversion_counter += len(left) - i
            j += 1

    f += left[i:]
    f += right[j:]   
    return f, inversion_counter

def mergesort(arr):
    global tot_count
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    sorted_arr, temp = merge(left, right)
    tot_count += temp

    return sorted_arr

if __name__ == '__main__':
    tot_count = 0
    n = int(input())
    a = list(map(int, input().split()))
    mergesort(a)
    print(tot_count)
