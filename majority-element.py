class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        majority_el = []
        unique = Counter(majority_el)
        boundary = len(nums)/3
        for num in nums:
            if ctr[num]>boundary and unique[num] == 0:
                majority_el.append(num)
                unique = Counter(majority_el)   
        return majority_el
             
