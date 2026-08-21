class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lst=[]
        for i in range(len(boxes)):
            count=0
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    count+=abs(i-j)
            lst.append(count)
        return lst
        