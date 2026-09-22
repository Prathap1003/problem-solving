class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        p=num
        while p>0:
            j=p%10
            if num%j==0:
                count+=1
            p//=10
        return count