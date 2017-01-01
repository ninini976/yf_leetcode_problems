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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum = 0;
        int carry = 0;
        ListNode* result = new ListNode(0);
        ListNode* current = result;
        while(true){
            if(l1 && l2){
                sum = l1->val + l2->val + carry;
                carry = sum / 10;
                current->next = new ListNode(sum%10);
                cout << sum%10;
                current = current->next;
                if(carry){
                    current->next = new ListNode(carry);
                }
                l1 = l1->next;
                l2 = l2->next;
            }else if(l1){
                sum = l1->val + carry;
                carry = sum / 10;
                current->next = new ListNode(sum%10);
                cout << sum%10;
                current = current->next;
                if(carry){
                    current->next = new ListNode(carry);
                }
                l1 = l1->next;
            }else if(l2){
                sum = l2->val + carry;
                carry = sum / 10;
                current->next = new ListNode(sum%10);
                cout << sum%10;
                current = current->next;
                if(carry){
                    current->next = new ListNode(carry);
                }
                l2 = l2->next;
            }else{
                break;
            }
        }
        return result->next;
    }
};
