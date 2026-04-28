class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      
        cnt = Counter(nums)
        duplicate = -1
        missing = -1
        for i in range(1, len(nums)+1):
            if i in cnt and cnt[i]==2:
                duplicate = i
            elif i not in nums:
                missing = i
     
        return [duplicate, missing]

        

        
