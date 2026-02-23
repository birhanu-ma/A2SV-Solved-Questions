import sys
input = sys.stdin.readline

def optimalPoint(n, list1):
    list1.sort()
    return list1[(n - 1) // 2]

n = int(input())
arr = list(map(int, input().split()))

print(optimalPoint(n, arr))
