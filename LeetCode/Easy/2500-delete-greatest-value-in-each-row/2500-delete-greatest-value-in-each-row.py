class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer=0
        length=len(grid[0])
        print(length)
        for i in range(length):
            val=0
            for row in range(len(grid)):
                val=max(val,max(grid[row]))
                grid[row].remove(max(grid[row]))
            answer+=val
        return answer


