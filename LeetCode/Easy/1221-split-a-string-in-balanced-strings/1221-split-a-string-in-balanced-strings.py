class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count=0
        l=0
        r=0
        l_count=0
        r_count=0
        while r<len(s):
            if s[r]=='R':
                r_count+=1
            else:
                l_count+=1
            if (r-l+1)%2==0 and r_count==l_count:
                count+=1
                l=r+1
            r+=1
        return count

        