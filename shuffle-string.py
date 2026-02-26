class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        map_to_list = [[indice[i], s[i]] for i in range(len(s))]
        map_to_list.sort(key:lambda a:a[0])
        return "".join(map_to_list)

        
