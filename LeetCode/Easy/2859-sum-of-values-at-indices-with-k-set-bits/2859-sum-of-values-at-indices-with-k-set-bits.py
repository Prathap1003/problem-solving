class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        answer=0
        for i in range(len(nums)):
            count=0
            s=i
            while i:
                i=i&(i-1)
                count+=1
            if count==k:
                answer+=nums[s]
            print(answer)
        return answer