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
            lst.append(ans)
            temp=temp.next
        res=head
        c=0
        i=0
        print(lst)

        while res.next!=None:
            if c==0:
                n1=ListNode(lst[i])
                i+=1
                c=1
                tel=res.next
                res.next=n1
                n1.next=tel
            else:
                c=0
            res=res.next
        return head

        
            


        

        