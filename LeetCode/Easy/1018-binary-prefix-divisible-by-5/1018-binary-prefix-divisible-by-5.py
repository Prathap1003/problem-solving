class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        lst=[]
        ans=0
        for val in nums:
            ans=ans<<1|val
            if ans%5==0:
                lst.append(True)
            else:
                lst.append(False)
        return lst
        