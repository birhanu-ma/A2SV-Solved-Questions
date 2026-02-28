class Solution:
    def findValidPair(self, s: str) -> str:
        s_list = [int(num) for num in s]
        ctr = Counter(s_list)
        valid_pair = []
        for i in range(len(s_list)-1):
            diff = abs(s_list[i]-s_list[i+1])
            if diff:
                if ctr[s_list[i]]==s_list[i] and ctr[s_list[i+1]] == s_list[i+1]:
                    valid_pair.append(s_list[i])
                    valid_pair.append(s_list[i+1])
                    return "".join(map(str,valid_pair))
        return ""


                


            
