class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        lst=[]
        for prime in nums:
            ans=-1
            for i in range(1,prime+1):
                if i|(i+1)==prime:
                    lst.append(i)
                    break
            else:
                lst.append(-1)
        return lst