class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        lst=[]
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
                lst.append(i)
            else:
                dic[i]=1
        return lst
        