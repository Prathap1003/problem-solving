class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower=-1
        last=-1
        l=0
        r=len(nums)-1
        lower=0
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                lower=mid
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                last=mid
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        if lower==-1 or last==-1:
            return [-1,-1]
        else:
            return [lower,last]
        
        