class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1]+nums[i])
        min_value = min(prefix_sum)
        if min_value < 0:
            return abs(min_value)+1
        elif min_value >= 0:
            return 1


