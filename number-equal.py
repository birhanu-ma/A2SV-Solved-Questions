from collections import Counter
def numberEqual(n, arr1, arr2):
    arr1_counter = Counter(arr1)
    arr2_counter = Counter(arr2)
    sum_equal_idx = 0
    for k, v in arr1_counter.items():
        sum_equal_idx += v*arr2_counter[k]
    return sum_equal_idx
n = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(numberEqual(n, arr1, arr2))


        
