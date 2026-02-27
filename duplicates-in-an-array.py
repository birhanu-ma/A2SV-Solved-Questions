class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        duplicates = []
        for k, v in counter.items():
            if v>=2:
                duplicates.append(k)
        return duplicates
    
        
