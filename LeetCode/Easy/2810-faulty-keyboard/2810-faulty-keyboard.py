class Solution:
    def finalString(self, s: str) -> str:
        string=""
        for i in s:
            if i=='i':
                string=string[::-1]
                continue
            string+=i
        return string
            
        