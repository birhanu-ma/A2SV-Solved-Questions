class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_magazin = Counter(magazine)
        count_ransomNote = Counter(ransomNote)
        for k, v in count_ransomNote.items():
            if count_magazin[k]<count_ransomNote[k]:
                return False
        return True
        
