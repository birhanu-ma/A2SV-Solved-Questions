class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD = 10**9 + 7
        
        def Pow(x, p):
            if p == 0:
                return 1
            
            half = Pow(x, p // 2)
            
            if p % 2 == 0:
                return (half * half) % MOD
            else:
                return (half * half * x) % MOD

        even_pos = (n + 1) // 2
        odd_pos = n // 2
        
        res_even = Pow(5, even_pos)
        res_odd = Pow(4, odd_pos)
        
        return (res_even * res_odd) % MOD
