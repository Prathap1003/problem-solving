class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        evens=[]
        odds=[]
        for i in nums1:
            if i&1==0:
                evens.append(i)
            else:
                odds.append(i)
        if not odds or not evens:
            return True
        if min(odds)<min(evens):
            return True
        else:
            return False
        