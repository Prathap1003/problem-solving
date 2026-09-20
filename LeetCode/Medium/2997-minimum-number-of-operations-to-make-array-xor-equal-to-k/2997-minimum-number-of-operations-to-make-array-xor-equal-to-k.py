class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer=0
        count=0
        for val in nums:
            answer^=val
        while answer>0 or k>0:
            if answer&1!=k&1:
                count+=1
            answer>>=1
            k>>=1
        return count

        