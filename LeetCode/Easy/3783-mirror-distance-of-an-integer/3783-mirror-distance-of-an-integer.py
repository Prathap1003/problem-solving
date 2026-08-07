class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev=0
        s=n
        while n>0:
            rev=rev*10+n%10
            n//=10
        return abs(rev-s)
        