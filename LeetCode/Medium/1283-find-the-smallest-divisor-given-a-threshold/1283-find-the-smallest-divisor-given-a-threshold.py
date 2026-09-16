class Solution:
    def solve(self,nums,mid,threshold):
        answer=0
        if mid==0:
            return False
        for val in nums:
            answer+=math.ceil(val/mid)
        return answer<=threshold
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=0
        r=max(nums)
        val=0
        while l<=r:
            mid=(l+r)//2
            if self.solve(nums,mid,threshold):
                val=mid
                r=mid-1
            else:
                l=mid+1
        return val
         
        