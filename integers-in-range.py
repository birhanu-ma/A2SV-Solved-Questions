class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
     
        for i in range(left,right+1):
            flag = False
            for j in range(len(ranges)):
                inner_list = sorted(ranges[j])
                if inner_list[0]<=i and i<=inner_list[1]:
                    flag = True
                    break
            if not flag:
                return False
        return True 



