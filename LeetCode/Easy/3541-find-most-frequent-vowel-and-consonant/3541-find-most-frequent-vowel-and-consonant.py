class Solution:
    def maxFreqSum(self, s: str) -> int:
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        vowel=0
        consonant=0
        for key , value in dic.items():
            if key in "aeiou":
                vowel=max(vowel,value)
            else:
                consonant=max(consonant,value)
        return vowel+consonant
        