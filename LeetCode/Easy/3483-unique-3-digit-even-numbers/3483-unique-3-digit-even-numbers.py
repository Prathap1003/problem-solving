import itertools as co
import math
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        values=(set(list(co.permutations(digits,3))))
        count=0
        for sets in values:
            val=int("".join(map(str,sets)))
            digit_count=len(str(val))
            if val&1==0 and digit_count==3:
                count+=1
        return count
        
        