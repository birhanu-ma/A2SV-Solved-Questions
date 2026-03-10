class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for folder in logs:
            if folder != "../" and folder!= "./":
                stack.append(folder)
            elif folder=="../":
                if stack:
                    stack.pop()
            else:
                continue
                
        return len(stack)
                
     
        
