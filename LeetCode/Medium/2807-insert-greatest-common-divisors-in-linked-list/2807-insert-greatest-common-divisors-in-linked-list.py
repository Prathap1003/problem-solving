# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def gcdfind(a,b):
    while b:
        a,b=b,a%b
    return a
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        lst=[]
        if head.next==None:
            return head
        while temp.next!=None:
            a=temp.val
            b=temp.next.val
            ans=gcdfind(a,b)
            node=ListNode(ans)
            va=temp.next
            temp.next=node
            node.next=va
            temp=temp.next.next
        return head


        
            


        

        