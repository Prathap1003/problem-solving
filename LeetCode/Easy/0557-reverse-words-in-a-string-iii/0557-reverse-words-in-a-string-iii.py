class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        string=""
        for word in s:
            string+=word[::-1]
            string+=' '
        return string[:-1]