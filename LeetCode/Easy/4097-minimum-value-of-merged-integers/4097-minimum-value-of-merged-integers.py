class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        minimum_value=100000000
        for i in range(0,len(nums)-1,2):
            print(i)
            value=nums[i]*10**(len(str(nums[i+1])))+nums[i+1]
            minimum_value=min(minimum_value,value)
        return minimum_value
        