class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        for j in range(len(s)-1):
            ans+=abs(int(ord(s[j])-int(ord(s[j+1]))))
        return ans
        