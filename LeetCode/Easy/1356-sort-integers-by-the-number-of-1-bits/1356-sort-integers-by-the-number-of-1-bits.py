class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic={}
        for val in arr:
            if val.bit_count() not in dic:
                dic[val.bit_count()]=[]
                dic[val.bit_count()].append(val)
            else:
                dic[val.bit_count()].append(val)
        lst=[]
        for key,value in sorted(dic.items()):
            lst+=sorted(value)
        return lst