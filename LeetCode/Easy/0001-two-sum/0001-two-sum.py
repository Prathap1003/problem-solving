class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst=[]
        s=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    lst.append(i)
                    lst.append(j)
                    s=1
                    return lst
                    break
            if s==1:
                break
            
        