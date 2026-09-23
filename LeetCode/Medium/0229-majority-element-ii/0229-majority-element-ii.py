class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        lst=[]
        n=len(nums)
        dic=collections.Counter(nums)
        print(dic)
        for key,value in dic.items():
            if value>(n//3):
                lst.append(key)
        return lst