#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        count_a = Counter(a)
        for num in b:
            if count_a[num] > 0:
                count_a[num] -= 1
            else:
                return False
        return True
    
    
    
    
