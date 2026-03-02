class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        answer = 0
        sum_even = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                answer+=nums[i]
        for value, idx in queries:
            old_value = nums[idx]

            if old_value%2==0:
                answer-=nums[idx]


            nums[idx]+=value
            new_value = nums[idx]

            if new_value%2==0:
                answer+=new_value
            sum_even.append(answer)
        return sum_even
        

        
