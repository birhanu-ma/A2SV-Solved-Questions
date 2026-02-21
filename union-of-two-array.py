class Solution:    
    def findUnion(self, a, b):
        # code here
        temp_union = sorted(a+b)
        union = []
        if temp_union:
            union.append(temp_union[0])
            for i in range(1,len(temp_union)):
                if temp_union[i-1]!=temp_union[i]:
                    union.append(temp_union[i])
            return union
        else:
            return []
            
     
                
        
