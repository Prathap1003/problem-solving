class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dic={}
        for key,value in knowledge:
            dic[key]=value
        f=0
        string=""
        l=0
        r=0
        while r<len(s):
            if s[r]=='(':
                f=1
                l=r+1
            elif s[r]==')':
                val=s[l:r]
                if val in dic:
                    string+=dic[val]
                else:
                    string+='?'
                f=0
            if f==0 and s[r]!=')':
                string+=s[r]
            r+=1
        return string
                