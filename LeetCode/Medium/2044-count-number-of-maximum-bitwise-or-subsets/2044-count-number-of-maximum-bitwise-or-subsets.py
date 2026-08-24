class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count=0
        answer=0
        return_value=0
        for i in range(2**len(nums)):
            j=0
            answer=0
            while i>0:
                if i&1>0:
                    answer|=nums[j]
                else:
                    pass
                j+=1
                i=i>>1
            count=max(count,answer)
        for i in range(2**len(nums)):
            j=0
            val=0
            while i>0:
                if i&1>0:
                    val|=nums[j]
                else:
                    pass
                j+=1
                i=i>>1
            if val==count:
                return_value+=1
        return return_value

        

        