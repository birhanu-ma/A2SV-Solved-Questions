class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        word_sum = 0
        for word in words:
            word_in_char = True
            for char in word:
                if word.count(char)> chars.count(char):
                    word_in_char = False
                    break
            if word_in_char:
                word_sum+=len(word)
        return word_sum
