class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for value in range(low,high+1):
            ans=len(str(value))
            if ans%2==1:
                continue
            right_sum=0
            left_sum=0
            left=ans//2
            right=ans//2
            while left:
                left_sum+=value%10
                value//=10
                left-=1
            while right:
                right_sum+=value%10
                value//=10
                right-=1
            if right_sum==left_sum:
                count+=1
        return count


        