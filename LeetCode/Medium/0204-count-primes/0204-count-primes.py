class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        if n<=3:
            return 1
        box = [True]*n
        box[0],box[1]=False,False
        for i in range(2,int(n**0.5+1)):
            if box[i]:
                for j in range(i*i,n,i):
                    box[j]=False
        return sum(box)
        
        
        