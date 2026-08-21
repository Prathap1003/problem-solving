class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        answer=requests[0]
        for i in range(1,len(requests)):
            answer+=abs(requests[i-1]-requests[i])
        return answer
        