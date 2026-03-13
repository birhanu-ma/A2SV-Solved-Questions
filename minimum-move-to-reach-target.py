class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        targ = target
        cnt  = 0
        while targ>1:
            if maxDoubles==0:
                cnt+=(targ-1)
                return cnt
            if targ%2==0 and maxDoubles>0:
                targ = targ//2
                maxDoubles-=1
                cnt+=1
            else:
                targ-=1
                cnt+=1
        return cnt





        


        
