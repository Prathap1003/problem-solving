class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        dic={}
        max_len=0
        max_fre=0
        while r<len(s):
            if s[r] not in dic:
                dic[s[r]]=1
                max_fre=max(max_fre,dic[s[r]])
            else:
                dic[s[r]]+=1
                max_fre=max(max_fre,dic[s[r]])
            if (r-l+1)-max_fre<=k:
                max_len=max(max_len,r-l+1)
            else:
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    del dic[s[l]]
                l+=1
            r+=1
        return max_len
        