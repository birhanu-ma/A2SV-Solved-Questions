import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        ans = []
        forward.append(1)
        current_prod = 0
        for i in range(len(nums)-1):
            current_prod = forward[i]*nums[i]
            forward.append(current_prod)
        backward = []
        backward.append(1)
        for i in range(len(nums)-1,0,-1):
            current_pro = backward[-1]*nums[i]
            backward.append(current_pro)
        backward.reverse()
        for i in range(len(forward)):
            ans.append(backward[i]*forward[i])
        
        return ans

        
