class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """

        position.sort()

        def helper(interval):
            ctr = 1
            left = 0
            for i in range(len(position)):
                if position[i]-position[left] >= interval:
                    ctr+=1
                    left=i

            return ctr >= m


        
        left = -1
        right = 10 ** 9 
        while left + 1 < right:
            mid = (right+left)//2
            if helper(mid):
                left = mid
            else:
                right = mid  
        return left          
           


        
