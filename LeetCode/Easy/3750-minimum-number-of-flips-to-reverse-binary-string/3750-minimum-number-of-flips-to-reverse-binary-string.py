class Solution:
    def minimumFlips(self, n: int) -> int:
        count=0
        s=bin(n)[2:]
        k=s[::-1]
        for i in range(len(k)):
            if s[i]!=k[i]:
                count+=1
        return count
        


        