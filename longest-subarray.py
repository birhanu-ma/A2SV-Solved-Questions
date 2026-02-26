class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        zero_in = 0
        for right in range(len(nums)):
            if nums[right] == 0 :
                zero_in += 1
            while zero_in >= 2:
                if nums[left] == 0:
                    zero_in -=1
                left+=1
            max_len = max(max_len, right-left+1)

        return max_len - 1
        
