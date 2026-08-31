class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n<=3:
            return []
        seive=[1]*n
        seive[0],seive[1]=0,0
        for i in range(2,int(n**0.5)+1):
            if seive[i]:
                for j in range(i*i,n,i):
                    if seive[j]:
                        seive[j]=0
        lst=[]
        for i in range(2,(len(seive)//2)+1):
            if seive[i] and seive[n-i]:
                seive[i]=0
                seive[n-i]=0
                lst.append([i,n-i])
        return lst
        