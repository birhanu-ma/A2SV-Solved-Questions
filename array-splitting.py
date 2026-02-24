import sys
input = sys.stdin.readline
def arraySplit(n, arr):
    k = n[1]
    cost=[]
    minimum_cost = 0
    for i in range(len(arr)-1):
        difference = abs(arr[i]-arr[i+1])
        cost.append(difference)
    cost.sort()
    for j in range(len(cost)-k+1):
        minimum_cost+=cost[j]
    return minimum_cost
n = list(map(int, input().split()))
arr = list(map(int, input().split()))

print(arraySplit(n, arr))
