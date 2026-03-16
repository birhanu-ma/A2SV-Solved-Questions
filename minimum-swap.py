class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
    
        xy = 0
        yx = 0

        for char1, char2 in zip(s1, s2):
            print(char1, char2)
            if char1 == 'x' and char2 == 'y':
                xy += 1
            elif char1 == 'y' and char2 == 'x':
                yx += 1

        if (xy + yx) % 2 != 0:
            return -1

        return xy // 2 + yx // 2 + (xy % 2) * 2
            
