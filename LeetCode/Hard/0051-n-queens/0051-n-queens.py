def isvalid(row,col,board,n):
    temp=row
    tem=col
    while temp>=0:
        if board[temp][col]=='Q':
            return False
        temp-=1
    temp=row
    while temp>=0 and tem<n:
        if board[temp][tem]=='Q':
            return False
        temp-=1
        tem+=1
    temp=row
    tem=col
    while temp>=0 and tem>=0:
        if board[temp][tem]=='Q':
            return False
        temp-=1
        tem-=1
    return True

def solve(row,res,board,n):
    if n==row:
        res.append([])
        print('hello')
        for i in board:
            res[-1].append("".join(i))
        return

    for col in range(n):
        if isvalid(row,col,board,n):
            board[row][col]='Q'
            solve(row+1,res,board,n)
            board[row][col]='.'
            
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res=[]
        board=[['.']*n for _ in range(n)]
        solve(0,res,board,n)
        return res

        