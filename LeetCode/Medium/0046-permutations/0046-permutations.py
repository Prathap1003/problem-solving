def genarate(idx,res,lst,check,nums):
    if len(lst)==len(nums):
        res.append(lst.copy())
        return
    if idx==len(nums):
        return
    for i in  range(len(nums)):
        if check[i]==0:
            lst.append(nums[i])
            check[i]=1
            genarate(idx+1,res,lst,check,nums)
            lst.pop()
            check[i]=0
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        lst=[]
        check=[0]*len(nums)
        genarate(0,res,lst,check,nums)
        return res

        