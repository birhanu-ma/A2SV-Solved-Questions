class Solution:
    def lastRemaining(self, n: int) -> int:
        
        def helper(start, step, n_current, left):
            if n_current == 1:
                return start
            
            if left:
                start += step
            else:
                if n_current % 2 == 1:
                    start += step
            
            n_current //= 2
            step *= 2
            

            return helper(start, step, n_current, not left)
        
        return helper(1, 1, n, True)
