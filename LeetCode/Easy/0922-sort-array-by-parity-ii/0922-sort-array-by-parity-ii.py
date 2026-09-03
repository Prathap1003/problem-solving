class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l=0
        r=1

        lst=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]&1==0:
                lst[l]=nums[i]
                l+=2
            else:
                lst[r]=nums[i]
                r+=2
        return lst


        
        