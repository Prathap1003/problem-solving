class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                lst.append(s[i])
            else:
                if not lst:
                    return False
                if lst[-1]=='(' and s[i]==')' or lst[-1]=='[' and s[i]==']' or lst[-1]=='{' and s[i]=='}':
                    lst.pop()
                else:
                    return False
        if lst:
            return False            
        return True



        
        
        