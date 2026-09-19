def cou(val):
    count=0
    while val:
        val>>=1
        count+=1
    return count
class Solution:
    def countMonobit(self, n: int) -> int:
        count=1
        if n+1&(n)==0:
            count+=(cou(n))
        else:
            count+=(cou(n)-1)
        return count

        