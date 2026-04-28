class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt = {0:0,1:0,2:0}
        for n in nums:
            cnt[n]+=1
        i = 0
        for color in cnt:
            for _ in range(cnt[color]):
                nums[i]=color
                i+=1
            
        
        
