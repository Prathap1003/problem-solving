def digit(num):
    answer=0
    while num>0:
        answer+=num%10
        num//=10
    return answer

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=0
        digit_sum=0
        for i in range(len(nums)):
            element_sum+=nums[i]
            digit_sum+=digit(nums[i])
        return abs(element_sum-digit_sum)
        