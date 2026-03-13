class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ctr = Counter(answers)
        min_num = 0
        for key, value in ctr.items():
            group_size = key+1
            num_group = (key+value)//group_size
            min_num  += num_group*group_size
            
        return min_num
        
