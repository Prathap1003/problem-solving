class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        first = a.bit_count()
        second = b.bit_count()
        if first >=second:
            return first*second
        else:
            return second//first