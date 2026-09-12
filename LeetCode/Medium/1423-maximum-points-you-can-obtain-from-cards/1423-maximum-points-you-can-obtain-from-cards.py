class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_points=sum(cardPoints[:k])
        total=max_points
        h=len(cardPoints)-1
        l=k-1
        for i in range(l,-1,-1):
            total-=cardPoints[i]
            total+=cardPoints[h]
            max_points=max(max_points,total)
            h-=1
        return max_points