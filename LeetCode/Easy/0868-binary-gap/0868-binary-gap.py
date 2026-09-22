class Solution:
    def binaryGap(self, n: int) -> int:
        ans=bin(n)[2:]
        l=0
        r=1
        max_len=0
        while r<len(ans):
            if ans[r]=='1':
                max_len=max(max_len,r-l)
                l=r
            r+=1
        return max_len

        