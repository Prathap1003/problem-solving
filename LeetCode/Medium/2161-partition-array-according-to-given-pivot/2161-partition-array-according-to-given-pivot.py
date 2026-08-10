class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lst=[]
        lst1=[]
        lst2=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                lst.append(nums[i])
            elif nums[i]>pivot:
                lst2.append(nums[i])
            else:
                lst1.append(nums[i])
        return lst+lst1+lst2
        