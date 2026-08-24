from collections import deque
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        que=deque(nums)
        for i in range(k):
            ans=nums.pop()
            que.appendleft(ans)
            que.pop()
        nums[:]=que
        

        
        