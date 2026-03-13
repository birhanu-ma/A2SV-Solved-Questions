class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n-2):
            if nums[i]==0:
                nums[i]=1
                if nums[i+1] == 0: 
                    nums[i+1]=1 
                else:
                    nums[i+1] =0
                if nums[i+2] == 0:
                    nums[i+2]=1 
                else:
                    nums[i+2] =0
                cnt+=1
            else:
                continue
        print(nums)
        if nums[n-1] == 1 and nums[n-2] == 1:
            return cnt
        else:
            return -1
        
