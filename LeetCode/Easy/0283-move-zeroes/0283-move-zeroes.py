class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=0
        l=len(nums)
        while r<l:
            if nums[r]==0:
                del nums[r]
                nums.append(0)
                l-=1
            else:
                r+=1
        