class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        string=sorted(s,key=lambda x:x[-1])
        string=[word[:-1] for word in string]
        return " ".join(string)