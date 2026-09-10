import collections as co
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic=co.Counter(s)
        for i in range(len(s)):
            if dic[s[i]]==1:
                return i
                break
        return -1
        
        