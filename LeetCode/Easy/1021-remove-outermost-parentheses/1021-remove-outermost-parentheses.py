class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        string=""
        l=0
        r=0
        while r<len(s):
            if s[r]=='(':
                count+=1
            else:
                count-=1
            if count==0:
                string+=s[l+1:r]
                l=r+1
            r+=1
        return string

        