class Solution:
    def splitNum(self, num: int) -> int:
        lst=[]
        while num>0:
            lst.append(num%10)
            num//=10
        lst.sort()
        l=0
        r=len(lst)-1
        answer=0
        st=''
        pt=""
        f=0
        for i in range(len(lst)):
            if f==0:
                st+=str(lst[i])
                f=1
            else:
                pt+=str(lst[i])
                f=0
        return int(st)+int(pt)




        