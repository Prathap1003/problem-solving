class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        dic=collections.Counter(nums)
        for val in dic.values():
            if val%2!=0:
                return False
        return True