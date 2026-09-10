class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=0
        r=0
        l=len(matrix[0])-1
        while (row<len(matrix)):
            l=0
            r=len(matrix[0])-1
            while l<=r:
                mid=(l+r)//2
                if target==matrix[row][mid]:
                    return True
                elif target<matrix[row][mid]:
                    r=mid-1
                else:
                    l=mid+1
            row+=1
        return False
        