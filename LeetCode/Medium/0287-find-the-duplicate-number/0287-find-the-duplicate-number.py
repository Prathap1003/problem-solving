class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        ans=0
        for val in nums:
            if ans&(1<<val):
                return val
            ans=ans|1<<val 