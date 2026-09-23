class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        lst=[nums[0]]
        for i in range(1,len(nums)):
            lst.append(lst[i-1]+nums[i])
        return lst
        