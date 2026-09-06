class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words=title.split()
        result=[word.title() if len(word)>2 else word.lower() for word in words]
        return " ".join(result)

        