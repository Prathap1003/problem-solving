class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        l=0
        r=0
        max_len=0
        lst=[-1]*256
        while r<len(s):
            if lst[ord(s[r])]!=-1:
                if lst[ord(s[r])]>=l:
                    l=lst[ord(s[r])]+1
            max_len=max(max_len,r-l+1)
            lst[ord(s[r])]=r
            r+=1
        return max_len


        
        