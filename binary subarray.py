class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sub_num = {0:1}
        total = 0
        count = 0

        for n in nums:
            total += n
            
            if total - goal in sub_num:
                count += sub_num[total-goal]
            
            sub_num[total] = 1 + sub_num.get(total, 0)
        return count
