class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        count = {0:1}
        prefix = 0
        total_subarray = 0
        for num in nums:
            prefix+=num
            reminder = prefix%k

            if reminder in count:
                total_subarray+=count[reminder]
                count[reminder]+=1
            else:
                count[reminder] = 1
        return total_subarray




