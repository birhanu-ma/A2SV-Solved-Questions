class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        target = len(nums) - k
        def quickselect(arr, k_idx):
            pivot = random.choice(arr)
            
            left =  [x for x in arr if x < pivot]
            mid =   [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            
            if k_idx < len(left):
                return quickselect(left, k_idx)
            elif k_idx < len(left) + len(mid):
                return mid[0]
            else:
                return quickselect(right, k_idx - len(left) - len(mid))
        
        return quickselect(nums, target)
