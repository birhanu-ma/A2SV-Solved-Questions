class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        diff = [0]*(len(s)+1)
        for start, end , direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start]+=val
            diff[end+1]-=val
            
        current_shift  = 0
        for i in range(len(s)):
             current_shift+=diff[i]
             new_char_idx = (ord(s[i]) - 97 + current_shift) % 26
             s[i] = chr(97 + new_char_idx)
        return "".join(s)



        
