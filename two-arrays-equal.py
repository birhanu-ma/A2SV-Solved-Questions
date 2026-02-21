class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a = sorted(a)
        b = sorted(b)
        for i in range(len(a)):
            if a[i]!=b[i]:
                return False
        return True
       
