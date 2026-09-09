class Solution:
    def countSegments(self, s: str) -> int:
        s=s.strip()
        if len(s)<1:
            return 0
        count=0
        words=0
        for i in range(len(s)):
            if s[i]!=' ':
                count+=1
            else:
                if count>=1:
                    words+=1
                    count=0
        return words+1

        