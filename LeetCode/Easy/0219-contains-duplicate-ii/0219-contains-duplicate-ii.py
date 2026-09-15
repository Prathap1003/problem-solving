class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=dic.get(nums[i],[])
            dic[nums[i]].append(i)
        print(dic)
        for key,lst in dic.items():
            if len(lst)<=1:
                continue
            else:
                for i in range(1,len(lst)):
                    if abs(lst[i-1]-lst[i])<=k:
                        return True
        return False

        