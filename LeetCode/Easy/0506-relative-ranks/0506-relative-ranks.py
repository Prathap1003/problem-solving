class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores=sorted(score,reverse=True)
        dic={}
        j=4
        medels=["Gold Medal","Silver Medal","Bronze Medal"]
        for i in range(len(score)):
            if i<=2:
                dic[scores[i]]=medels[i]
            else:
                dic[scores[i]]=str(j)
                j+=1
        for i in range(len(score)):
            score[i]=dic[score[i]]
        return score
        


        
        