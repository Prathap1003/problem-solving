class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        total=0
        dic={}
        l=0
        r=0
        while r<len(fruits):
            if fruits[r] not in dic:
                dic[fruits[r]]=1
            else:
                dic[fruits[r]]+=1
            if len(dic)<=2:
                total=max(total,r-l+1)
            else:
                dic[fruits[l]]-=1
                if dic[fruits[l]]==0:
                    del dic[fruits[l]]
                l+=1
            r+=1
        return total
        