class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        answer=0
        for i in range(1,2**len(nums)):
            res=0
            j=0
            while i>0:
                if i&1>0:
                    res=res^nums[j]
                j+=1
                i=i>>1
            print(res,end=" ")
            answer+=res
        return answer


        
        