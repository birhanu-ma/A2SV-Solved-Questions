class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        left = 0
        ctr = defaultdict(int)
        distinct_count = 0
        cnr = 0
        prefix = 0 
        for i in range(len(nums)):
            if ctr[nums[i]] == 0:
                distinct_count += 1
            ctr[nums[i]] += 1
 
            if distinct_count > k:
                ctr[nums[left]] -= 1
                distinct_count -= 1
                left += 1
                prefix = 0
            
            while ctr[nums[left]] > 1:
                prefix += 1
                ctr[nums[left]] -= 1
                left += 1
                
            
            if distinct_count == k:
                cnr += (prefix + 1)
                
        return cnr
