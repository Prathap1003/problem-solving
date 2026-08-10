class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        lst=[]
        for i in range(len(order)):
            if order[i] in friends:
                lst.append(order[i])
        return lst