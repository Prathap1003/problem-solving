class Solution:
    def splitArray(self, nums: List[int]) -> int:
        if len(nums)<=2:
            sum1=0
            for i in range(len(nums)):
                sum1+=nums[i]
            return abs(sum1)
        seive=[1]*len(nums)
        seive[0],seive[1]=0,0
        for i in range(2,int(len(nums)**0.5)+1):
            if seive[i]:
                for j in range(i*i,len(nums),i):
                    if seive[j]:
                        seive[j]=0
        sum1,sum2=0,0
        for i in range(len(nums)):
            if seive[i]:
                sum1+=nums[i]
            else:
                sum2+=nums[i]
        return abs(sum1-sum2)

        