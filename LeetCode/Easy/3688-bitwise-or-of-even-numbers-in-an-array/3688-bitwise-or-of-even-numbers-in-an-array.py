class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        answer=0
        for i in nums:
            if i%2==0:
                answer|=i
        return answer
        