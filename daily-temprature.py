class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n 
        
        for i in range(n):
        
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day_index = stack.pop()
                
                ans[prev_day_index] = i - prev_day_index
                
            stack.append(i)
            
        return ans


