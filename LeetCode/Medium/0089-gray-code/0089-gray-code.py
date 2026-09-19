class Solution:
    def grayCode(self, n: int) -> List[int]:
        lst=[]
        s=2**n-1
        for i in range(0,s+1):
            answer=i^(i>>1)
            lst.append(answer)
        return lst
        