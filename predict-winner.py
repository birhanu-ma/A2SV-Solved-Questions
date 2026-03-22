class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """       
        def get_max_diff(i, j):
            
            if i == j:
                return nums[i]
            pick_left = nums[i] - get_max_diff(i + 1, j)

            pick_right = nums[j] - get_max_diff(i, j - 1)
            
            return max(pick_left, pick_right)
      
        return get_max_diff(0, len(nums) - 1) >= 0

