/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    if (head==NULL){
        return head;
    }
    struct ListNode *slow=head;
    while (slow!=NULL && slow->val==val ){
        head=head->next;
        slow=slow->next;
    }
    struct ListNode *temp=head;
    while (temp!=NULL){
    if (temp->next!=NULL && temp->next->val==val){
    temp->next=temp->next->next;}
    else{
    temp=temp->next;}}

    return head;


}