def mostSocialDistanced(t,  n, nums):
    ans = []
    
    ans.append(nums[0])
    for i in range(1, len(nums)-1):
        if nums[i-1]<nums[i]>nums[i+1] or nums[i-1]>nums[i]<nums[i+1]:
            ans.append(nums[i])
    ans.append(nums[n-1])
    print (len(ans))
    return ans
        
        
    
    
    
    
    
    
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(*mostSocialDistanced(t, n, nums))
