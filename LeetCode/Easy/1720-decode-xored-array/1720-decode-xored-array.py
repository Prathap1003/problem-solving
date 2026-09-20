class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        lst=[first]
        for i in range(len(encoded)):
            lst.append(encoded[i]^lst[i])
        return lst
