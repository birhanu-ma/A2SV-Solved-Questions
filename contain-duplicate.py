class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        nums.sort()
        for i in range(size-1):
                if nums[i] == nums[i+1]:
                    return True
        return False
        
