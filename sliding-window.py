from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        max_sliding = []
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] <nums:
                queue.pop()
            queue.append(i)
            if queue[0]==i-k:
                queue.popleft()
            if i >= k - 1:
                max_sliding.append(nums[queue[0]])
                
        return max_sliding
 
