from collections import deque
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer=max(nums)
        lst=[]
        lst=deque()
        s=32
        while s:
            hi=0
            for i in range(len(nums)):
                hi+=(nums[i]&1)
                nums[i]=nums[i]>>1
            lst.appendleft(str(hi%3))
            s-=1
        val=int("".join(lst),2)
        if val>=2**31:
            val-=2**32
        return val
        
                

        
        