def numberOfSegment(n, arr):
    s = n[1]
    n = len(arr)
    window = 0
    ans = 0
    left = 0
    for right in range(n):
        window+=arr[right]
        while window>s:
            window-=arr[left]
            left+=1
        ans+=(right-left+1)
    return ans
n = list(map(int, input().split()))
arr  = list(map(int, input().split()))
print(numberOfSegment(n, arr))
