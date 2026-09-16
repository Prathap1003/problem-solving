class Solution:

    def solve(self,w,mid,days):
        
        day = 1
        ans = 0
        for i in w:
            if i>mid:
                return False
            ans+=i
            if ans>mid:
                ans=i
                day+=1
        print(day)
        return days>=day
    def shipWithinDays(self, w: List[int], days: int) -> int:
        #1 2 2 3 4 4
        #
       # w.sort()
        l= min(w)
        r =sum(w)
        val =0
        while(l <= r):
            mid=(l+r)//2
            print(l,r,mid)
            if self.solve(w,mid,days):
                val=mid
                r=mid-1
            else:
                l=mid+1
        return val
        
        