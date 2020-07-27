# Uses python3
import sys

def optimal(a):
    optimum =[]
    while a!= []:
        points = []
        for segment in a:
            points.append(segment[1])
        minimum = min(points)

        index =[]
        for i in range(len(a)):
            if a[i][0] <= minimum and a[i][1] >= minimum:
                index.append(i)

        x =[]    
        
        for i in range(len(a)):
            if i not in index:
                x.append(a[i])

        a = x
        optimum.append(minimum)
    return optimum

        
n = int(input())
a = []
for i in range(n):
    data = list(map(int,input().split()))
    a.append(data)

points = optimal(a)
print(len(points))
for i in range(len(points)):
    print(points[i], end=' ')
