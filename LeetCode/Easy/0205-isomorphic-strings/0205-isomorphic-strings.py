class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        if len(set(s))!=len(set(t)):
            return False
        for i in range(len(s)):
            dic.setdefault(s[i],set()).add(t[i])
        print(dic)
        for value in dic.values():
            if len(value)>=2:
                return False
        return True

        




        