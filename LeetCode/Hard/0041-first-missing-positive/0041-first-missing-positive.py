class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        answer=0
        val=max(nums)+1
        if max(nums)<=0:
            return 1
        lls=set(nums)
        for i in range(1,val+1):
            if i not in lls:
                return i
