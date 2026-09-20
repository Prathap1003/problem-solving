class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        if num<1:
            return 0
        while num:
            if num%2==1:
                num-=1
                count+=1
            count+=1
            num>>=1
        return count-1