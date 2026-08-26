class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic={}
        string="abcdefghijklmnopqrstuvwxyz"
        j=0
        for i in key:
            if i!=" " and i not in dic:
                dic[i]=string[j]
                j+=1
        dic[" "]=" "
        strin=""
        for k in message:
            strin+=dic[k]
        return strin



        