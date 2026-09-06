class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count=0
        val=0
        for value in nums:
            val+=value
            if val==0:
                count+=1
        return count

        