class Solution:
    def validStrings(self, n: int) -> List[str]:
        lst=[]
        for i in range(0,2**n):
            ans=format(i,f'0{n}b')
            string=""
            s=n
            count=0
            answer=0
            j=0
            while s:
                if ans[j]=='1':
                    count=0
                else:
                    count+=1
                answer=max(answer,count)
                j+=1
                s-=1
            if answer<2:
                lst.append(ans)
            else:
                pass
        return lst

                

