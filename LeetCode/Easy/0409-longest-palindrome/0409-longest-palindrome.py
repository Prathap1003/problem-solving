class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer=0
        dic={}
        for string in s:
            dic[string]=dic.get(string,0)+1
        max_odd=0
        print(dic)
        lst=[0]
        for value in dic.values():
            if value%2==0:
                answer+=value
            else:
                answer+=(value-1)
                max_odd=max(max_odd,value)
        if max_odd:
            return answer+1
        return answer