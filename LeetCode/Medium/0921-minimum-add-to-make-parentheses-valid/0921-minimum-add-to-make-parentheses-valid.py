class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        lst=[]
        for i in s:
            if i=='(':
                lst.append(i)
            else:
                if lst:
                    if lst[-1]=='(':
                        lst.pop()
                    else:
                        lst.append(i)
                else:
                    lst.append(i)
        return len(lst)
        