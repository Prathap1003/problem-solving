class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        eeights=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i]!=eeights[i]:
                count+=1
        return count
        