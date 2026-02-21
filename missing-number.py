class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missed =True
        for i in range(len(nums)+1):
            for j in range(len(nums)):
                if i == nums[j]:
                    missed = False
                    break
                else:
                    missed = True
            if missed:
                return i
            
