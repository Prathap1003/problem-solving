class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index=0
        for i in range(len(word)):
            if word[i]==ch:
                index=i
                break
        print(index)
        print(word[:index+1])
        print(word[index+1:])
        return word[:index+1][::-1]+word[index+1:]