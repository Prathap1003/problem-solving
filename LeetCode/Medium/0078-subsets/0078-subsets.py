class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst=[]
        n=len(nums)
        lst.append([])
        for i in range(1,2**n):
            pst=[]
            j=0
            while i>0:
                if i&1>0:
                    pst.append(nums[j])
                j+=1
                i>>=1
            lst.append(pst)
        return lst
