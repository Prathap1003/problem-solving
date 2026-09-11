class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry=0
        string=""
        ran=min(len(num1),len(num2))
        i=-1
        while ran:
            val=int(int(num1[i])+int(num2[i]))+carry
           # print(val)
            act=val%10
            carry=val//10
            string+=str((act))
            ran-=1
            i-=1
        #print(string)
        remai=max(len(num1),len(num2))-min(len(num1),len(num2))
        if len(num1)>len(num2):
            arr=num1
        else:
            arr=num2
        i=remai-1
        print(remai)
        while remai:
            val=int(arr[i])+carry
            act=val%10
            carry=val//10
            string+=str((act))
            remai-=1
            i-=1
        if carry!=0:
            string+=str(carry)
        return string[::-1]
        

        

        