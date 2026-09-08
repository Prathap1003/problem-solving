class Solution:
    def replaceDigits(self, s: str) -> str:
        string=""
        for i in range(len(s)):
            if i&1>0:
                string+=(chr(ord(s[i-1])+int(s[i])))
            else:
                string+=s[i]
        return string
        