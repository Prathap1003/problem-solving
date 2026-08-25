class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums=set(nums)
        j=1
        while True:
            ans=k*j
            if ans not in nums:
                return ans
                break
            j+=1

        