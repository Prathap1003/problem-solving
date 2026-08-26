class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        ast=0
        for i in s:
            if i=="|":
                ast+=1
            if ast%2==0:
                if i=='*':
                    count+=1
        return count

        