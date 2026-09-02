class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k==len(nums):
            return sum(nums)/k
        initial=sum(nums[:k])
        max_value=initial/k
        for i in range(1,len(nums)-k+1):
            initial-=nums[i-1]
            initial+=nums[i+k-1]
            max_value=max(max_value,initial/k)
        return max_value


        