class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit=0
        p=n
        product=1
        while n>0:
            digit+=n%10
            product*=n%10
            n//=10
        return p%(digit+product)==0
        