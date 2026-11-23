class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        dic=collections.Counter(word)
        print(dic)
        for key,value in dic.items():
            if 97<=ord(key)<=122:
                if key.upper() in dic and dic[key.upper()]!=0 and dic[key]!=0:
                    count+=1
                    dic[key]=0
                    dic[key.upper()]=0
            else:
                if key.lower() in dic and dic[key.lower()]!=0 and dic[key]!=0:
                    count+=1
                    dic[key.lower()]=0
                    dic[key]=0
        return count
        