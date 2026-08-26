class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count=0
        hashmap=defaultdict(int)
        for j in nums:
            count+=hashmap[j+k]
            count+=hashmap[j-k]
            hashmap[j]+=1
        return count
        