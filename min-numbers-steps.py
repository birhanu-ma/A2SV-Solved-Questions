class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_counter = Counter(t)
        s_counter =Counter(s)
        step = 0
        for char in s_counter:
           if s_counter[char]>t_counter[char]:
            step+=s_counter[char]-t_counter[char]
        return step

