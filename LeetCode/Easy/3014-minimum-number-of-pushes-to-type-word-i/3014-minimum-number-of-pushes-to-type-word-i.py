class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word)<=8:
            return len(word)
        else:
            count=0
            s=len(word)
            i=1
            while s>=8:
                count+=8*i
                s-=8
                i+=1
            count+=(s%8)*i

            return count

                
        