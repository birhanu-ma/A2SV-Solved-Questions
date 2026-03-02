class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        original = []
        changed.sort()
        counter = Counter(changed)
        for num in changed:
            if counter[num] == 0:
                continue
            counter[num] -= 1
            if counter[num * 2] > 0:
                counter[num * 2] -= 1
                original.append(num)
            else:
                return []
        return original if len(original) == len(changed) // 2 else []
        



            



        
