class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans  = ""
        count = Counter(s)
        print(count)
        for i in range(len(order)):
            ch = order[i]
            if ch in s:
                ans += ch * count[ch]
        for k, v in count.items():
            if k not in order:
                ans += k * v
        
        return ans

                    
        
        
