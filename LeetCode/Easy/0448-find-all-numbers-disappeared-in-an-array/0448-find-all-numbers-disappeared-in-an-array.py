class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        dic=defaultdict(int)
        lst=[]
        dic=collections.Counter(nums)
        for i in range(1,len(nums)+1):
            if dic[i]==0:
                lst.append(i)
        return lst
