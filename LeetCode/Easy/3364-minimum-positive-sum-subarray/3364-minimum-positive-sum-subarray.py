class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        answer=1000000
        for i in range(l,r+1):
            present_value=sum(nums[:i])
            print(present_value)
            if present_value>0:
                answer=min(present_value,answer)
            for j in range(len(nums)-i):
                if nums[j]<0:
                    present_value+=abs(nums[j])
                else:
                    present_value-=nums[j]
                present_value+=nums[i+j]
                print(present_value)
                if present_value>0:
                    answer=min(present_value,answer)
        if answer==1000000:
            return -1
        return answer

        