class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = (num-3)%3
        m = (num-3)//3
        if not n:
            return [m+n, m+n+1, m+n+2]
        return []
      
