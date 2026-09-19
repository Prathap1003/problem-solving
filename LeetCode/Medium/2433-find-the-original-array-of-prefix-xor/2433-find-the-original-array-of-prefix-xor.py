class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        lst=[]
        lst.append(pref[0])
        for i in range(1,len(pref)):
            answer=pref[i-1]^pref[i]
            lst.append(answer)
        return lst
        