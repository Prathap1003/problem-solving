class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        answer=0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    answer+=abs(i-j)
        return answer

        