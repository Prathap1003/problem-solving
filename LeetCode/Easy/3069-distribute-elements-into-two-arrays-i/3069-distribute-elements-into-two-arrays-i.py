class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        lst=[nums[0]]
        lst1=[nums[1]]
        for i in range(2,len(nums)):
            if lst[-1]>lst1[-1]:
                lst.append(nums[i])
            else:
                lst1.append(nums[i])
        return lst+lst1
# last element of arr1 greather than the lst element of arr2 

        