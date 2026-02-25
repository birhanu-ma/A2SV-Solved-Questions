class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        srt = 0
        end = len(needle)
        while end<=len(haystack):
            sliced_haystack = haystack[srt:end]
            if needle == sliced_haystack:
                return srt
            srt+=1
            end+=1
        

        
