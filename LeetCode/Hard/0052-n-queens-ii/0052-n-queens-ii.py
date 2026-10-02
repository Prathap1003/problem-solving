def solve(row,board,c,ld,rd,n):
    if row==n:
        return 1
    count=0
    for col in range(n):
        if c[col]==0 and rd[row+col]==0 and ld[row-col+(n-1)]==0:
            board[row][col]=1
            c[col],rd[row+col],ld[row-col+(n-1)]=1,1,1
            count+=solve(row+1,board,c,ld,rd,n)
            board[row][col]=0
            c[col],rd[row+col],ld[row-col+(n-1)]=0,0,0
    return count
class Solution:
    def totalNQueens(self, n: int) -> int:
        c=[0]*n
        rd=[0]*(2*n)
        ld=[0]*(2*n)
        board=[[0]*n for i in range(n)]
        val=solve(0,board,c,ld,rd,n)
        return val