class Solution(object):
    def __init__(self):
        self.com = []
        self.ans = []
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start):
            if len(self.com) == k:
                self.ans.append(list(self.com)) 
                return
            
            for i in range(start, n + 1):
                self.com.append(i)    
                backtrack(i + 1)      
                self.com.pop()       

        backtrack(1)
        return self.ans
