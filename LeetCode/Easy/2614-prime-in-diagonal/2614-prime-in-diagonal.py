class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        s=(max(max(row) for row in nums))
        box=[1]*(s+1)
        box[0],box[1]=0,0
        for i in range(2,int(s**0.5)+1):
            if box[i]:
                for j in range(i*i,s+1,i):
                    box[j]=0
        maximum=0
        for i in range(len(nums[0])):
            if box[nums[i][i]]:
                maximum=max(maximum,nums[i][i])
            if box[nums[i][len(nums[0])-i-1]]:
                maximum=max(maximum,nums[i][len(nums[0])-i-1])                
        return maximum

        