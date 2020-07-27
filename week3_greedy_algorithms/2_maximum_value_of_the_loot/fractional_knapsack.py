# Uses python3
import sys

def get_optimal_value(capacity, weights, values,n):
    value = 0
    valueperw = []
    for i in range(n):
        valueperw.append(values[i]/weights[i])
    while capacity>0 and n >0:
        for j in range(len(valueperw)):
            if valueperw[j] == max(valueperw):
                wg = min(weights[j],capacity)
                fraction = wg/weights[j]
                value = value + values[j]*fraction
                capacity = capacity - wg
                values.pop(j)
                weights.pop(j)
                valueperw.pop(j)
                n = n-1
                break
    return value


data = list(map(int, input().split()))
n, capacity = data[0:2]
weights=[]
values=[]
for _ in range(n):
    value , weight = map(int, input().split())
    values.append(value)
    weights.append(weight)

opt_value = get_optimal_value(capacity, weights, values,n)
print("{:.4f}".format(opt_value))
