class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_count=0
        checking=(k)*(k+1)//2
        lst=set()
        for i in range(len(nums)-1,-1,-1):
            if checking==0:
                return min_count
            if nums[i]<=k and nums[i] not in lst:
                checking-=nums[i]
                lst.add(nums[i])
            min_count+=1
        return min_count