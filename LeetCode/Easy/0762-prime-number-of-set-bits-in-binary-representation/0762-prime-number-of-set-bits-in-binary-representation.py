class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        seive=[1]*(32)
        seive[0],seive[1]=0,0
        for i in range(2,int(32**0.5)+1):
            if seive[i]:
                for j in range(i*i,32,i):
                    if seive[j]:
                        seive[j]=0
        lst=[]
        for i in range(left,right+1):
            lst.append(i.bit_count())
        count=0
        for val in lst:
            if seive[val]:
                count+=1
        return count
        