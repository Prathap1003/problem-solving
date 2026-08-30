class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        val=max(nums)
        seive=[1]*(val+1)
        seive[0],seive[1]=0,0
        for i in range (2,int(val**0.5)+1):
            if seive[i]:
                for j in range(i*i,val+1,i):
                    if seive[j]:
                        seive[j]=0
        lst=[]
        for i in range(len(nums)):
            if seive[nums[i]]:
                lst.append(i)
        return max(lst)-min(lst)       