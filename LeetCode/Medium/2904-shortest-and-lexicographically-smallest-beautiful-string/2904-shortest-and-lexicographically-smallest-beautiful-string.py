class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        string=""
        lst=[]
        min_length=100
        for i in range(len(s)):
            if s[i]=="1":
                strin="1"
                count=1
                if count==k:
                    lst.append(strin)
                    min_length=min(min_length,len(strin))
                    continue
                for j in range(i+1,len(s)):
                    if s[j]=='1':
                        count+=1
                    strin+=s[j]
                    if count>k:
                        break
                    if count==k:
                        min_length=min(min_length,len(strin))
                        lst.append(strin)
                        break
        print(min_length)
        print(lst)
        lls=[]
        for j in lst:
            if min_length==len(j):
                lls.append(j)
            else:
                pass
        print(lst)
        if not lst:
            return string
        else:
            return str(min(lls))
        


        