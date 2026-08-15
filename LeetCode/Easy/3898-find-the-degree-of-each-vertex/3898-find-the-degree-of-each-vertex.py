class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        lst=[]
        for row in range(len(matrix)):
            count=0
            for column in range(len(matrix)):
                if matrix[row][column]!=0:
                    count+=1
            lst.append(count)
        return lst
        