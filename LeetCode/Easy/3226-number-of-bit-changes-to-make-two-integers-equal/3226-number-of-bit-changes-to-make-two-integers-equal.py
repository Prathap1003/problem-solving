class Solution:
    def minChanges(self, n: int, k: int) -> int:
        count=0
        count2=0
        s=n
        l=k
        while n>0:
            if n&1>0:
                count+=1
            n=n>>1
        while k>0:
            if k&1>0:
                count2+=1
            k=k>>1
        if (s&l) != l:
            return -1
        else:
            return count-count2
        
                

        
        