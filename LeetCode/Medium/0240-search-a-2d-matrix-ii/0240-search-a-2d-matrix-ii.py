class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        r=0
        l=col-1
        while (r<row and l>=0):
            current=matrix[r][l]
            if target==current:
                return True
            elif current<target:
                r+=1
            else:
                l-=1
        return False

        