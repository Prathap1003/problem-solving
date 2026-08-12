class Solution:
    def smallestValue(self, n: int) -> int:
        pp=n
        box=[0]*(n+1)
        for i in range(1,n+1):
            box[i]=i
        for i in range(2,int(n**0.5)+1):
            if box[i]==i:
                for j in range(i*i,n+1,i):
                    if box[j]==j:
                        box[j]=i
        res=box[n]
        while box[n]!=n:
            ans=0
            while n>1:
                ans+=box[n]
                n//=box[n]
            if ans==pp:
                return ans
                break
            n=ans
            res=ans
        return res

        
        


        
        
        