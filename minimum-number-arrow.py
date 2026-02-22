class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda points : points[1])
        num_arrow = 1
        arrow = points[0][1]
        for [start, end] in points:
            if start>arrow:
                num_arrow +=1
                arrow = end
        return num_arrow 
