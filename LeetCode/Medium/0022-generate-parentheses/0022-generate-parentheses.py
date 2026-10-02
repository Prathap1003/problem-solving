def genarate(open,close,res,lst,n):
    if open==close==n:
        res.append("".join(lst))
        return
    if open<n:
        lst.append('(')
        genarate(open+1,close,res,lst,n)
        lst.pop()
    if close<open:
        lst.append(')')
        genarate(open,close+1,res,lst,n)
        lst.pop()
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        lst=[]
        genarate(0,0,res,lst,n)
        return res
        
        
        