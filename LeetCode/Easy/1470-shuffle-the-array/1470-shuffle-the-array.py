class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst=[]
        for j in range(len(nums)//2):
            lst.append(nums[j])
            lst.append(nums[n+j])
        return lst
            

        