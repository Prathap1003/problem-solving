class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s=1
        ma=0
        ans=0
        pns=0
        count=0
        i=0
        for j in range(i+1,len(nums)):
            if nums[j]-nums[i]==s:
                count+=1
                s+=1
                if count>ma:
                    ans=i
                    pns=j
                    ma=count
            else:
                break
                count=0
                s=1
        print(ans,pns)
        hello=sum(nums[ans:pns+1])
        while True:
            if hello not in nums:
                return hello
                break
            else:
                hello+=1
        
        

            


        