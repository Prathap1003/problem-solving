class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        box=[True]*101
        box[1],box[0]=False,False
        for i in range(2,int(100**0.5)+1):
            if box[i]:
                for j in range(i*i,101,i):
                    box[j]=False
        dic={}
        for j in nums:
            dic[j]=dic.get(j,0)+1
        for k in dic.values():
            if box[k]:
                return True
        return False

        