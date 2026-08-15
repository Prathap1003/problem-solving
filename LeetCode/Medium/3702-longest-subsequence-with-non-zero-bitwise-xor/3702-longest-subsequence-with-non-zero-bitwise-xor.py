class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans=0
        f=0
        for i in nums:
            ans^=i
            if ans>f:
                f=1
        if f==0:
            return 0
        if ans==0:
            return len(nums)-1
        else:
            return len(nums)
        