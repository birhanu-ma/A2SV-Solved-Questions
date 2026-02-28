class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            nums = set(nums)
            nums = list(nums)
            nums.sort()
            left = 0
            right = 1
            ctr = 0
            length = 0
            if not nums:
                return 0
            if len(nums) == 1:
                return 1
            for right in range(len(nums)-1):
                if nums[right]+1==nums[right+1]:
                    ctr+=1
                else:
                    length = max(ctr, length)
                    ctr=0
                length = max(ctr, length)
            return length+1




