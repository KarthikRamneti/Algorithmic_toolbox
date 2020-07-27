# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    Big_list = []
    for i in range(len(starts)):
        Big_list.append((starts[i],"l"))
        Big_list.append((ends[i],"r"))

    for i in points:
        Big_list.append((i,"p"))

    Big_list.sort()
    point_seg = dict()
    cnt =0
    for x in Big_list:
        if x[1] == 'l':
            cnt += 1
        elif x[1] == 'r':
            cnt -= 1
        else:
            point_seg[x[0]] = cnt
    return point_seg

if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    m = data[1]
    starts = []
    ends = []
    for i in range(n):
        s = list(map(int, input().split()))
        starts.append(s[0])
        ends.append(s[1])
    points = list(map(int, input().split()))
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in points:
        print(cnt[x], end=' ')
