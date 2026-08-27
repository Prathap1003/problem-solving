class Solution:
    def missingInteger(self, num: List[int]) -> int:
        s=num[0]
        for i in range(1,len(num)):
            if num[i]==num[i-1]+1:
                s+=num[i]
            else:
                break
        
        while s in num:
            s+=1 
        return s

            


        