class Solution:
    def reverseParentheses(self, s: str) -> str:
        count=s.count("(")
        res=len(s)
        while count:
            l=0
            r=0
            while r<res:
                if s[r]=='(':
                    l=r+1
                elif s[r]==')':
                    hello=s[l:r]
                    s=s[:l-1]+hello[::-1]+s[r+1:]
                    break
                r+=1
            count-=1
        return s