class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        dic={}
        if len(set(pattern))!=len(set(s)) or len(pattern)!=len(s):
            return False
        for key,value in zip(pattern,s):
            dic.setdefault(key,set()).add(value)
            if len(dic[key])>1:
                return False
        return True