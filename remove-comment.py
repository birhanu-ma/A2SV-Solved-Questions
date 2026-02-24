class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        comment_removed = []
        temp = []
        block_comment = False

        for i in range(len(source)):
            j = 0
            if not block_comment:
                temp = []
            
            while j < len(source[i]):
                if not block_comment and source[i][j:j+2] == "//":
                    break
                elif not block_comment and source[i][j:j+2] == "/*":
                    block_comment = True
                    j += 2
                    continue
                elif block_comment and source[i][j:j+2] == "*/":
                    block_comment = False
                    j += 2
                    continue
                elif not block_comment:
                    temp.append(source[i][j])
                
                j += 1
            if not block_comment and temp:
                comment_removed.append("".join(temp))
        
        return comment_removed
