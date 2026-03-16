class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
  
        words = s.split()

        if len(pattern) != len(words):
            return False

        cnt_words = defaultdict(list)
        cnt_pattern = defaultdict(list)

        for idx, val in enumerate(words):
            cnt_words[val].append(idx)
            
        for idx, val in enumerate(pattern):
            cnt_pattern[val].append(idx)

        for p_char, w_word in zip(pattern, words):
            if cnt_pattern[p_char] != cnt_words[w_word]:
                return False
                
        return True
