class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst=[i for i in range(1,n+1)]


        i=0

        while True:
            if len(lst)==1:
                return lst[0]
            i = (i+k-1)%n
            lst.pop(i)
            n-=1
                   