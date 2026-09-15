class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[l]==nums[mid]==nums[r]:
                l+=1
                r-=1
                continue
            elif nums[mid]<=nums[r]:
                r=mid
            else:
                l=mid+1
        return nums[mid]
        