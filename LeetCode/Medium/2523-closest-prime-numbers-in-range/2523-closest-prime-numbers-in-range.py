class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        seive=[1]*(right+1)
        seive[0],seive[1]=0,0
        for i in range(2,int(right**0.5)+1):
            if seive[i]:
                for j in range(i*i,right+1,i):
                    seive[j]=0
        lst=[]
        for i in range(left,right+1):
            if seive[i]:
                lst.append(i)
        if len(lst)<=1:
            return [-1,-1]
        min_value=lst[1]-lst[0]
        hello=[]
        hello.append(lst[0])
        hello.append(lst[1])
        for i in range(1,len(lst)):
            if lst[i]-lst[i-1]<min_value:
                hello[0],hello[1]=lst[i-1],lst[i]
                min_value=lst[i]-lst[i-1]
        return hello



        