class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        max_radius = 0        
        def find_closest_index(target, arr):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low  

        for house in houses:
            idx = find_closest_index(house, heaters)
            
            dist_right = heaters[idx] - house if idx < len(heaters) else float('inf')
            
            dist_left = house - heaters[idx - 1] if idx > 0 else float('inf')
            

            current_min_dist = min(dist_left, dist_right)
            max_radius = max(max_radius, current_min_dist)
            
        return max_radius
