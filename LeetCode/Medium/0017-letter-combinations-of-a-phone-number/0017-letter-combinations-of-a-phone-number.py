def genarate(digits,dic,idx,res,temp):
    if idx==len(digits):
        val="".join(temp)
        res.append(val)
        return 
    for i in (dic[digits[idx]]):
        temp.append(i)
        genarate(digits,dic,idx+1,res,temp)
        temp.pop()
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res=[]
        temp=[]
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        genarate(digits,dic,0,res,temp)
        return res
        