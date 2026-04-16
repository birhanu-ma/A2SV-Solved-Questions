class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        candies.sort()
        def helper(mid):
            ctr = 0
            for i in range(len(candies)):
                ctr+=candies[i]//mid
            return ctr>=k

        
        left = 0
        right = 10 ** 9
        while left + 1 < right:
            mid = (left+right)//2
            if helper(mid):
                left = mid
            else:
                right=mid
        return left
           
