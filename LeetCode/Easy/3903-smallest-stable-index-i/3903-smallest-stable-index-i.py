class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            val=max(nums[:i+1])
            val2=min(nums[i:])
            if (val-val2)<=k:
                return i
        return -1

        

        