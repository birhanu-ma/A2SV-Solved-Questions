class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = list(range(1, n+1))
        dq = deque(lst)
        def helper(dq, k):
            if len(dq)==1:
                return dq[0]
            for _ in range(k-1):
                tail = dq.popleft()
                dq.append(tail)
            dq.popleft()
            return helper(dq,k)
        return helper(dq , k)
           
       
        
