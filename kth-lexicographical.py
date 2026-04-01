class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        chars = ["a", "b","c"]
        if k > 3*(2**(n-1)):
            return ""
        def backtrack(path):
            if len(res)==k:
                return
            if len(path)==n and path not in res:
                res.append("".join(path[:]))
                return
            for char in chars:
                if not path or path[-1]!= char:
                    path.append(char)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return res[k-1]
            


        
