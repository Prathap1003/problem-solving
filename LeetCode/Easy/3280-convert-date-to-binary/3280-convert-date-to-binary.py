class Solution:
    def convertDateToBinary(self, date: str) -> str:
        string=""
        res=""
        for i in range(len(date)):
            if ord(date[i])>=48 and ord(date[i])<=57:
                res+=date[i]
            else:
                ans=int(res)
                string+=format(ans,'0b')
                string+='-'
                res=""
        string+=format(int(date[len(date)-2:]),'0b')
        return string


        