class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini=36
        for i in nums:
            ans=0
            while i>0:
                ans+=i%10
                i//=10
            mini=min(mini,ans)
        return mini

        