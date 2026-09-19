
def function(i,nums,answer,lst):
    if len(nums)==i:
        lst.append(answer.copy())
        return
    answer.append(nums[i])
    function(i+1,nums,answer,lst)
    answer.pop()
    function(i+1,nums,answer,lst)
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        answer=[]
        lst=[]
        function(0,nums,answer,lst)
        prev=[]
        for val in lst:
            val.sort()
        lst.sort()
        pst=lst.copy()
        print(pst)
        for val in pst:
            if prev==val:
                lst.remove(val)
            prev=val
        lst.append([])
        return lst
