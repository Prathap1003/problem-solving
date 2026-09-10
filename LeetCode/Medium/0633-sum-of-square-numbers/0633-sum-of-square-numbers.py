class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=int(c**0.5)
        while l<=r:
            ans=l*l+r*r
            if ans==c:
                return True
            elif ans<c:
                l+=1
            else:
                r-=1
        return False
        