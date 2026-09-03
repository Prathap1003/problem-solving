class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_even=1000000000
        min_odd=1000000000
        for i in nums1:
            if i&1==0:
                min_even=min(min_even,i)
            else:
                min_odd=min(min_odd,i)
        if min_odd==1000000000 or min_even==1000000000:
            return True
        if min_odd<min_even:
            return True
        else:
            return False
        