class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        lst=[]
        for i in range(len(index)):
            if len(lst)-1<index[i]:
                lst.append(nums[i])
            else:
                lst.insert(index[i],nums[i])
        return lst
