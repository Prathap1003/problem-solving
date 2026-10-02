def genarate(idx,res,lst,n,k,values):
    if len(lst)==k:
        res.append(lst.copy())
        return
    if idx==n:
        return
    lst.append(values[idx])
    genarate(idx+1,res,lst,n,k,values)
    lst.pop()
    genarate(idx+1,res,lst,n,k,values)
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        lst=[]
        values=[i for i in range(1,n+1)]
        genarate(0,res,lst,n,k,values)
        return res
        