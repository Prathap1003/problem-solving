class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for key,value in dic.items():
            if value>=2:
                pass
            else:
                k-=1
                if k==0:
                    return key
        return ""
        