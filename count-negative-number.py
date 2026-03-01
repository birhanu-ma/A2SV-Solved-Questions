class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ctr = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j])
                if grid[i][j]<0:

                    ctr+=1
        return ctr

        
