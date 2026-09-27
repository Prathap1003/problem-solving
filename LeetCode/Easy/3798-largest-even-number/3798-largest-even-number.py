class Solution:
    def largestEven(self, s: str) -> str:
        if not s:
            return ""
        if int(s[-1])%2==0:
            return s
        else:
            s=s[:len(s)-1]
            return self.largestEven(s)
