class Solution:
    def minimumPushes(self, word: str) -> int:
        dic={}
        for j in word:
            dic[j]=dic.get(j,0)+1
        lst=[]
        for i in dic.values():
            lst.append(i)
        lst.sort()
        i=1
        count=0
        answer=0
        for value in range(len(lst)-1,-1,-1):
            answer+=i*lst[value]
            count+=1
            if count==8:
                i+=1
                count=0
        return answer

        

        