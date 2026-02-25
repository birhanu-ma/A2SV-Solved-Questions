class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry_sum = 0
        skill_sum = 0
        left = 0
        right = len(skill)-1
        skill_sum = skill[left]+skill[right]
        while left<right:
            if skill[left]+skill[right]==skill_sum:
                chemistry_sum+=(skill[left]*skill[right])
                left+=1
                right-=1
            else :
                return -1
        return chemistry_sum


        
