class Solution:
    def reverseDegree(self, s: str) -> int:
        answer=0
        j=1
        for i in s:
            answer+=((26-(ord(i)-ord('a')))*j)
            j+=1
        return answer

        