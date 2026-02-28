class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ctr_word1 = Counter(word1)
        ctr_word2 = Counter(word2)
        ctr_word1_values = [value for k, value in ctr_word1.items()]
        ctr_word2_values = [value for k, value in ctr_word2.items()]
        ctr_word1_values.sort()
        ctr_word2_values.sort()
        for char in ctr_word1:
            if ctr_word2[char] == 0:
                return False
        if ctr_word1_values == ctr_word2_values:
            return True
        return False


        
