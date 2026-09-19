class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic={}
        for char in s:
            if char not in dic:
                dic[char]=1
            else:
                return char
        