class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        array=[]
        for i in range(len(nums)):
            if nums[i]==target:
                array.append(i)
        return array