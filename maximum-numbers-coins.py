class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        n = len(piles)//3
        max_coin = 0
        for i in range(len(piles)-n):
            if i%2 != 0:
                max_coin+=piles[i]               
        return max_coin


        
