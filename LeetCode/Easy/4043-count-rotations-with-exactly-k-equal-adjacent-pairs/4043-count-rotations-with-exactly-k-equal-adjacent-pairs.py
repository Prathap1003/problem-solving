class Solution:
    def countRotations(self, s: str, k: int) -> int:
        count=0
        for i in range(len(s)):
            ss=s[i:]+s[:i]
            lalalalaala=0
            for j in range(len(ss)-1):
                if ss[j]==ss[j+1]:
                    lalalalaala+=1
            if lalalalaala==k:
                count+=1
        return count
                    
        
        
        