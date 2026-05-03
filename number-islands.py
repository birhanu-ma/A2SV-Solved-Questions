class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        column = len(grid[0])
        islands = 0
        visited = set()
        def dfs(r,c):
            if (r<0 or c<0 or r==row or c==column or grid[r][c]!="1"):
                return
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            if (r,c) not in visited:
                if grid[r][c]=="1":
                    visited.add((r,c))
                    for dr,dc in directions:
                        dfs(dr+r,dc+c)
                    
        for r in range(row):
            for c in range(column):
                if (grid[r][c]=="1" and (r, c) not in visited):
                    dfs(r,c)
                    islands+=1
        return islands
