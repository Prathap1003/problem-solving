class Solution:
    def bool(self,boom,m,k,mid):
        count=0
        another=0
        for val in boom:
            if val<=mid:
                count+=1
            else:
                count=0
            if count==k:
                count=0
                another+=1
        return another>=m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        l=0
        r=max(bloomDay)
        val=0
        while l<=r:
            mid=(l+r)//2
            if self.bool(bloomDay,m,k,mid):
                r=mid-1
                val=mid
            else:
                l=mid+1
        return val
