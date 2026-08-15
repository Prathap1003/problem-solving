class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        lst=[]
        k=0
        for i in words:
            if x in i:
                lst.append(k)
            k+=1
        return lst
        