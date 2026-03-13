class Solution:
    def minOperations(self, nums):
        n = len(nums)
        flip = 0
        flip_end = [0] * n  
        operations = 0
        for i in range(n):
            if i >= 3:
                flip -= flip_end[i - 3] 
            if (nums[i] + flip) % 2 == 0:
                if i > n - 3:
                    return -1
                operations += 1
                flip += 1
                flip_end[i] = 1  
        return operations
