class Solution:
    def reverseBits(self, n: int) -> int:
        answer=0
        s=32
        while s:
            if n:
                j=n&1
            else:
                j=0
            answer=(answer<<1)|j
            n=n>>1
            s-=1
        return answer
        

        