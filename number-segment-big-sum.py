
def numberSegment(n, arr):
    s = n[1]
    n = len(arr)
    ans = 0
    current_sum = 0
    right = 0
    for left in range(n):
        while right < n and current_sum < s:
            current_sum += arr[right]
            right += 1
        if current_sum >= s:
            ans += (n - right + 1)
        current_sum -= arr[left]
    return ans

n = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(numberSegment(n,arr))
