class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        lst=[['#']*n for i in range (m)]
        for i in range(n-1):
            lst[0][i]='.'
        for i in range(m):
            lst[i][n-1]='.'
        pst=[]
        for row in lst:
            pst.append("".join(row))
        return pst
            