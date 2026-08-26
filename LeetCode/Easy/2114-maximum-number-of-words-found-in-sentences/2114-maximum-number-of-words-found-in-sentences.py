class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        value=0
        for sentence in sentences:
            value=max(value,len(re.findall(r' ',sentence)))
        return value+1
        