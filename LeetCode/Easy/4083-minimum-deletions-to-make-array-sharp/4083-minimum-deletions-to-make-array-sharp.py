class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        answer=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                answer+=1
        return answer
        