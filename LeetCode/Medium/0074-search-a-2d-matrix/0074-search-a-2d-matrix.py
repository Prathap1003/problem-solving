class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        s=0
        row=len(matrix)-1
        col=len(matrix[0])-1
        print(col)
        ans=0
        while l<=row:
            mid=(l+row)//2
            print(mid,row,col)
            print("prathap")
            if matrix[mid][0]<=target<=matrix[mid][col]:
                ans=mid
                break
            elif matrix[mid][col]>target:
                row=mid-1
            else:
                l=mid+1
        while s<=col:
            m=(s+col)//2
            if matrix[ans][m]==target:
                return True
            elif matrix[ans][m]>target:
                col=m-1
            else:
                s=m+1
        return False

                

