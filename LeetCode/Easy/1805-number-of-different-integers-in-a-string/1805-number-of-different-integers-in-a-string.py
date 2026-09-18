class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        lst=map(int,re.findall(r'\d+',word))
        return len(set(lst))
        

        