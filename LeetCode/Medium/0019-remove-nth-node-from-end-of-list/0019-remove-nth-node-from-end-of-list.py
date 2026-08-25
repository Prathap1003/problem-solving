# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        if count==1 and n==1:
            return None
        answer=count-n
        print(answer)
        hello=head
        if count==n:
            head=head.next
            return head
        for i in range(answer-1):
            if hello.next==None:
                return head
            hello=hello.next
        if hello.next==None:
            return head
        hello.next=hello.next.next
        return head