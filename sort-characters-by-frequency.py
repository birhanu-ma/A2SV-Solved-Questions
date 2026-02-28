class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        temp = ""
        for i in range(len(ctr)):
            key, count = ctr.most_common(1)[0]
            temp+=key*count
            del ctr[key]
        return temp


        
