 /**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 struct ListNode *newnoded(int value){
    struct ListNode *newnode;
    newnode=(struct ListNode*)malloc(sizeof(struct ListNode));
    newnode->val=value;
    newnode->next=NULL;
    return newnode;
 }
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
struct ListNode *head = NULL, *tail = NULL;
int carry = 0;

while (l1 != NULL || l2 != NULL || carry) {
    int x = (l1 != NULL) ? l1->val : 0;
    int y = (l2 != NULL) ? l2->val : 0;

    int s = x + y + carry;
    carry = s / 10;

    struct ListNode *newnode = newnoded(s % 10);

    if (head == NULL) {
        head = tail = newnode;
    } else {
        tail->next = newnode;
        tail = newnode;
    }

    if (l1) l1 = l1->next;
    if (l2) l2 = l2->next;
}

return head;
}