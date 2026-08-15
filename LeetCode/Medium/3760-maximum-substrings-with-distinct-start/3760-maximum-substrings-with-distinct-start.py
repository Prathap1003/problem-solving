class Solution:
    def maxDistinct(self, s: str) -> int:
        answer=0
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        return len(dic)
        