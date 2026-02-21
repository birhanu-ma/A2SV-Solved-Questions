class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lst_idx_sum = 10**18
        word = ["temp"]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j] and i+j<lst_idx_sum:
                    word.pop()
                    word.append(list1[i])
                    lst_idx_sum = i+j
                elif list1[i] == list2[j] and i+j==lst_idx_sum:
                    word.append(list1[i])
                else:
                    continue
        return word

        
