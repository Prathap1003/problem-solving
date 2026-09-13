class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_one=0
        l=0
        r=0
        zeros=0
        while r<len(nums):
            if nums[r]==0:
                zeros+=1
            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l=l+1
            else:
                max_one=max(max_one,r-l+1)
            r+=1
        return max_one

        