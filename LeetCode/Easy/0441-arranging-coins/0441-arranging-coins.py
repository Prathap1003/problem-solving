class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        i=1
        val=0
        while val<=n:
            count+=1
            val+=i
            i+=1
        return count-1

        