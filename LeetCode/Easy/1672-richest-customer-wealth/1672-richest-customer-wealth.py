class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_value=0
        for i in range(len(accounts)):
            val=0
            for j in range(len(accounts[i])):
                val+=accounts[i][j]
            max_value=max(max_value,val)
        return max_value
        