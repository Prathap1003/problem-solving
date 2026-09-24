class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        val=10000
        nums.sort()
        n=len(nums)
        for i in range(n):
            avg=((nums[i]+nums[n-i-1])/2)
            val=min(val,avg)
        return val
        