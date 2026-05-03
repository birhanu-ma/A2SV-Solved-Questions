class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(heights)
        col = len(heights[0])
        res = []
        def dfs(r,c, visited):
            reach_p = False
            reach_a = False
          
            if r==0 or c == 0:
                reach_p=True
            if r==row-1 or c==col-1:
                reach_a = True

                
            visited.add((r, c))
            direction = [(1,0),(-1,0),(0,1),(0,-1)]


            for (dr, dc) in direction:
                if 0<=dr+r<row and 0<=dc+c<col and (dr+r, dc+c) not in visited and heights[r][c]>=heights[dr+r][dc+c]:
                    p, a = dfs(dr+r, dc+c, visited)
                    reach_p = reach_p or p
                    reach_a = reach_a or a
                if reach_p and reach_a:
                    break

            return reach_p, reach_a


                



        for r in range(row):
            for c in range(col):

                p,a = dfs(r, c, set())
                if p and a:
                    res.append([r,c])
                
        return res


            


        
        
