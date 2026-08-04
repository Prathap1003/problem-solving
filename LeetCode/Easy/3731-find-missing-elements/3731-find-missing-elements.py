class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=min(nums)
        k=max(nums)
        for i in range(s,k+1):
            if i in nums:
                nums.remove(i)
            else:
                nums.append(i)
        return nums
        