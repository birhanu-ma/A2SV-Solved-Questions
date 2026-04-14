class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
       
        left = 0
        right = len(matrix)*len(matrix[0])-1
        while right>=left:
            mid = (left+right)//2
            i = mid//len(matrix[0])
            j = mid%len(matrix[0])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j]>=target:
                right = mid-1
            else:
                left=mid+1
        return False
      
        
            
