class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(len(nums)):
            ans=abs(sum(nums[:i])-(sum(nums[i:])-nums[i]))
            lst.append(ans)
        return lst

        