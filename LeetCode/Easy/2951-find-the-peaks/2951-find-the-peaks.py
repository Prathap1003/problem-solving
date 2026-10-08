class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        lst=[]
        if len(mountain)<=2:
            return []
        for i in range(1,len(mountain)-1):
            if mountain[i-1]<mountain[i]>mountain[i+1]:
                lst.append(i)
        return lst
        