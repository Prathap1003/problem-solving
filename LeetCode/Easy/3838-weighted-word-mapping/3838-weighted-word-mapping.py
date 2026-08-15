class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        string=""
        stringfor="abcdefghijklmnopqrstuvwxyz"
        for i in words:
            ans=0
            for j in range(len(i)):
                ans+=weights[ord(i[j])-ord('a')]
            print(ans)
            string+=stringfor[-(ans%26)-1]
        return string

        