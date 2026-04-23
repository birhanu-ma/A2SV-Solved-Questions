class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            if self.can_ship(weights, days, mid):
                right = mid
            else:
                left = mid + 1
                
        return left

    def can_ship(self, weights, days, capacity):
        current_days = 1
        current_load = 0
        
        for w in weights:
            if current_load + w > capacity:
                current_days += 1
                current_load = w
            else:
                current_load += w
        
        return current_days <= days



        
        
