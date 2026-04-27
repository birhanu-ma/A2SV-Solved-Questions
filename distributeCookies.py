class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """

        cookies.sort(reverse=True)
        
        self.unfair = float("inf")
        dist = [0] * k

        def backtrack(i):
            if max(dist) >= self.unfair:
                return

            if i == len(cookies):
                self.unfair = min(self.unfair, max(dist))
                return

            for j in range(k):
   
                if j > 0 and dist[j] == dist[j-1]:
                    continue
                
                dist[j] += cookies[i]
                backtrack(i + 1)
                dist[j] -= cookies[i]

        backtrack(0)
        return self.unfair
