class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        n=10**3
        spf=[0]*(n+1)
        for i in range(1,n+1):
            spf[i]=i
        for j in range(2,int(n**0.5)+1):
            if spf[j]==j:
                for k in range(j*j,n+1,j):
                    if spf[k]==k:
                        spf[k]=j
        dic={}
        for j in nums:
            while j>1:
                if spf[j] in dic:
                    dic[spf[j]]+=1
                else:
                    dic[spf[j]]=1
                j//=spf[j]
        ans=0
        for key, value in dic.items():
            if key:
                ans+=1
        return ans
        
        
            