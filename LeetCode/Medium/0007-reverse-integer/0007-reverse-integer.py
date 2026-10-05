def reverse(x):
    rev=0
    while x>0:
        j=x%10
        rev=rev*10+j
        x//=10
    return rev
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x=-1*x
            res=reverse(x)*-1
        else:
            res=reverse(x)
        if res<-2**31 or res>2**31:
            return 0
        return res

        
        