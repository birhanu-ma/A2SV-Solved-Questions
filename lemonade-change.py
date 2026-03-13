class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt_5 = 0
        cnt_10 = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                cnt_5+=1
            elif bills[i]==10 and cnt_5 !=0:
                cnt_5-=1
                cnt_10+=1
            elif bills[i]==20 and cnt_10!=0 and cnt_5!=0:
                cnt_10-=1
                cnt_5-=1
            elif bills[i] == 20 and cnt_5>=3:
                cnt_5-=3
            else:
                return False
        return True
        
