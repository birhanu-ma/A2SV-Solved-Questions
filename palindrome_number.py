class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        right =len(x)-1
        left = 0
        while left <= right:
            if x[left]!=x[right]:
                return False
            right-=1
            left+=1
            
        return True
