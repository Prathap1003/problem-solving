class Solution:
    def isFascinating(self, n: int) -> bool:
        string=(str(n)+str(n*2)+str(n*3))
        dic={}
        for i in string:
            if i=='0':
                return False
                break
            if i in dic:
                dic[i]+=1
                return False
                break
            else:
                dic[i]=1
        return True


        