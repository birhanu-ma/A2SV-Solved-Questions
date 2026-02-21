class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = [strs[0]]
        temp = []
        for i in range(len(strs)):
            for j in range(min(len(prefix[0]),len(strs[i]))):
                if strs[i][j]==prefix[0][j]:
                    temp.append(prefix[0][j])
                else:
                    break
            prefix = ["".join(temp)]
            temp =[]
        return prefix[0]
                    
        
        
