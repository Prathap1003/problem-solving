class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i=n
        while i>0:
            pro=1
            temp=i
            while temp>0:
                pro*=temp%10
                temp//=10
            if pro%t==0:
                return i
                break
            i+=1
        