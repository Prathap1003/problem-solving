class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=set(allowed)
        count=0
        for word in words:
            if len(ans|set(word))==len(ans):
                count+=1
        return count

        