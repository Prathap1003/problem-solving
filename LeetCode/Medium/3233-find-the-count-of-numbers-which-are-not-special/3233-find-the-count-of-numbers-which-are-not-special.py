class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        actual_range=r-l+1
        box=[1]*(int(r**0.5)+1)
        box[0],box[1]=0,0
        for i in range(2,int(r**0.5)+1):
            if box[i]:
                for j in range(i*i,int(r**0.5)+1,i):
                    box[j]=0
        count=0
        print(box)
        for j in range(int(l**0.5),int(r**0.5)+1):
            if box[j] and l<=j*j<=r :
                count+=1
        return actual_range-count   