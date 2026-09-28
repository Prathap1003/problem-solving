class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        answer=0
        for i in s:
            if i=='(':
                ans+=1
            elif i==')':
                ans-=1
            answer=max(answer,ans)
        return answer