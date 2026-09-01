class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(len(s)-1):
            if abs((ord(s[i])-ord('0'))-(ord(s[i+1])-ord('0')))>2:
                return False
                break
        else:
            return True   
        