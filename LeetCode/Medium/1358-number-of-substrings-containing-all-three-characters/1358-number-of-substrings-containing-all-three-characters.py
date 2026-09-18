class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        dic={}
        a,b,c=-1,-1,-1
        r=0
        while r<len(s):
            if s[r]=='a':
                a=r
            elif s[r]=='b':
                b=r
            else:
                c=r
            if a!=-1 and b!=-1 and c!=-1:
                count+=(min(a,b,c)+1)
            r+=1
        return count
            
        