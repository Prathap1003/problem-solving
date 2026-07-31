class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        #110010
        #543210
        lst=[]
        i=0
        even=0
        odd=0
        while n>0:
            if n&1>0 and i%2==0:
                even+=1
            if n&1>0 and i%2==1:
                odd+=1
            i+=1
            n=n>>1
        lst.extend([even,odd])
        return lst

        