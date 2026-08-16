class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if len(f)==1:
            if f[0]==0:
                if n<=1:
                    return True
                else:
                    return False
            else:
                if n==0:
                    return True
                else:
                    return False
        if f[0]==0 and f[1]==0:
            f[0]=1
            n-=1
        if f[-1]==0 and f[-2]==0:
            f[-1]=1
            n-=1
        for i in range(1,len(f)-1):
            if f[i-1]==f[i]==f[i+1]==0:
                f[i]=1
                n-=1
        if n<=0:
            return True
        else:
            return False
