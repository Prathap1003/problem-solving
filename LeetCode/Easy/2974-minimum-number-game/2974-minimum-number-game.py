class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        lst=[]
        s=len(nums)//2
        while s:
            if nums:
                alice=min(nums)
                nums.remove(min(nums))
            if nums:
                bob=min(nums)
                nums.remove(min(nums))
            lst.append(bob)
            lst.append(alice)
            s-=1
        return lst

        