class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ctr = 0
        num_ctr_lst = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]>nums[j]:
                    ctr+=1
            num_ctr_lst.append(ctr)
            ctr=0
        return num_ctr_lst
        
