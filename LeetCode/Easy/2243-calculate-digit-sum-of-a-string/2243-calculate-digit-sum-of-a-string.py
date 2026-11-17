def digit_sum(string):
    value=0
    for j in string:
        value+=int(j)
    return value
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        answer=''
        if len(s)<=k:
            return s
        for i in range(0,len(s),k):
            digit=digit_sum(s[i:i+k])
            answer+=str(digit)
        if len(answer)<=k:
            return answer
        else:
            return self.digitSum(answer,k)

        