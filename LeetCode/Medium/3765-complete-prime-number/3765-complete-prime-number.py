class Solution:
    def completePrime(self, num: int) -> bool:
        s=(int(num**0.5)+1)
        seive=[1]*s
        seive[0],seive[1]=0,0
        for i in range(2,s):
            if seive[i]:
                for j in range(i*i,s,i):
                    if seive[j]:
                        seive[j]=0
        lst=[]
        for i in range(len(seive)):
            if seive[i]:
                lst.append(i)
        prefix=0
        suffix=0
        pre_div=10**(len(str(num))-1)
        val=num
        suf_div=10
        pst=[]
        while pre_div:
            j=num//pre_div
            prefix=prefix*10+j
            num=num%pre_div
            pre_div//=10
            suffix=val%suf_div
            suf_div*=10
            if prefix not in pst:
                pst.append(prefix)
            if suffix not in pst:
                pst.append(suffix)
        for value in pst:
            if value<=s-1:
                if seive[value]!=1:
                    return False
            else:
                for j in lst:
                    if value%j==0:
                        return False
        return True


            



        