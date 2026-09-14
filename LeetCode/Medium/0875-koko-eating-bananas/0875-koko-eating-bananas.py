class Solution:
    def solve(self,val,piles,h):
        hours=0
        if val==0:
            return False
        for hour in piles:
            if hour<=val:
                hours+=1
            elif hour%val==0:
                hours+=(hour//val)
            else:
                hours+=((hour//val)+1)
        return hours<=h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=0
        r=sum(piles)
        value=0
        while l<=r:
            mid=(l+r)//2
            if self.solve(mid,piles,h):
                value=mid
                r=mid-1
            else:
                l=mid+1
        return value

        