class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        lst=len(nums)
        ans=0
        if len(nums)==k:
            return max(nums)
        elif k==1:
            ans=0
            for i in range(len(nums)):
                if nums.count(nums[i])==1:
                    ans=max(ans,nums[i])
            if ans:
                return ans
            else:
                return -1

        else:
            ans=0
            pns=1
            if nums.count(nums[0])==1:
                ans=max(ans,nums[0])
                if ans==0:
                    pns=0
            if nums.count(nums[-1])==1:
                ans=max(ans,nums[-1])
                if ans==0:
                    pns=0
            if pns==0 and ans==0:
                return 0
            if ans:
                return ans
            else:
                return -1
        