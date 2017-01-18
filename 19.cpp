/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* index1 = head;
        ListNode* index2 = head;
        for(int i = 0; i < n-1; i++){
            index2 = index2->next;
        }
        if(!index2->next){ // index2 is already the end of the list, need to remove head
            ListNode* newhead = head->next;
            return newhead;
        }else{
            ListNode* pre;
            while(index2->next){
                index2 = index2->next;
                pre = index1;
                index1 = index1->next;
            }
            pre->next = index1->next;
            return head;
        }
    }
};
