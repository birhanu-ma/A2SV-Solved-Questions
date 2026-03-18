class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        last_boundary = nums[n - 1]
        total_operations = 0
        
        for i in range(n - 2, -1, -1):
            if nums[i] > last_boundary:

                num_elements = (nums[i] + last_boundary - 1) // last_boundary
                

                total_operations += (num_elements - 1)
                

                last_boundary = nums[i] // num_elements
            else:
                last_boundary = nums[i]
                
        return total_operations
