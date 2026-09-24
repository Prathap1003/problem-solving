class Solution:
    def prathap(self,num):
        ans=0
        while num:
            ans+=num%10
            num//=10
        return ans
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if self.prathap(nums[i])==i:
                return i
        return -1

        

        