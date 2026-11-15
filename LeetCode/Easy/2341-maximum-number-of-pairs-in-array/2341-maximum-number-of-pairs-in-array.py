class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        dic=collections.Counter(nums)
        answer1,answer2=0,0
        for value,key in dic.items():
            answer1+=key//2
            answer2+=key%2
        return [answer1,answer2]
        