class Solution:
    def minPartitions(self, n: str) -> int:
        maximum_digit=0
        for i in n:
            maximum_digit=max(maximum_digit,int(i))
        return maximum_digit

        