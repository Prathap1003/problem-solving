def genarate(idx,can,lst,res,target):
    if idx==len(can):
        if target==0:
            res.append(lst.copy())
        return
    if target>=can[idx]:
        lst.append(can[idx])
        genarate(idx,can,lst,res,target-can[idx])
        lst.pop()
    genarate(idx+1,can,lst,res,target)
class Solution:
    def combinationSum(self, can: list[int], target: int) -> list[list[int]]:
        res=[]
        lst=[]
        genarate(0,can,lst,res,target)
        return res
        