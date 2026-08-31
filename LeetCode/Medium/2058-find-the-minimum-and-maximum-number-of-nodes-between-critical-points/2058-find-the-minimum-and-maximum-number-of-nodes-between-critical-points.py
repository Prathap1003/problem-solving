# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        initial=0
        hlo=head
        ans=1
        count=0
        while hlo:
            count+=1
            hlo=hlo.next
        if count<=2:
            return [-1,-1]
        min_value=count
        max_value=0
        temp=head
        prev=temp.val
        ans+=1
        temp=temp.next
        check_count=0
        min_count=count
        max_count=0
        while temp.next!=None:
            if (temp.val>prev and temp.val>temp.next.val) or (temp.val<prev and temp.val<temp.next.val):
                print("Prathap")
                min_count=min(ans,min_count)
                max_count=max(ans,max_count)
                check_count+=1
                if check_count==2:
                    min_value=min(abs(ans-initial),min_value)
                    check_count-=1
                initial=ans
            ans+=1
            prev=temp.val
            temp=temp.next
        if min_count==max_count or max_count==0:
            return [-1,-1]
        return [min_value,abs(min_count-max_count)]
        

        
        