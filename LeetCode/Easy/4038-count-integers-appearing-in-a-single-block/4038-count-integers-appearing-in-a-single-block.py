class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]]=[i]
        count=0
        for key,value in dic.items():
            if len(value)==1:
                count+=1
            else:
                f=1
                for i in range(1,len(value)):
                    if value[i]-value[i-1]!=1:
                        f=0
                        break
                if f:
                    count+=1
        return count
        