class Solution:
    def minMoves(self, nums: List[int]) -> int:
        val=max(nums)
        answer=0
        for i in nums:
            answer+=(val-i)
        return answer
        