/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *l3 = new ListNode();
        ListNode *l4 = l3;
        int flag = 0;
        bool f3 = true;
        bool f4 = true;
        while(true)
        {
            //ListNode *l4 = new ListNode();
            if(l1->next && l2->next){
                l3->val = l1->val + l2->val + flag;
                l1 = l1->next;
                l2 = l2->next;
                if(l3->val >= 10){
                    l3->val = l3->val % 10;
                    flag = 1;
                }
                else
                    flag = 0;
                l3->next = new ListNode(0);
                l3 = l3->next;
            }
            else if(l1->next && !l2->next){
                if(f4)
                    l3->val = l1->val + l2->val + flag;
                else
                    l3->val = l1->val + flag;
                l1 = l1->next;
                f4 = false;
                if(l3->val >= 10){
                    l3->val = l3->val % 10;
                    flag = 1;
                }
                else
                    flag = 0;
                l3->next = new ListNode(0);
                l3 = l3->next;
            }
            else if(l2->next && !l1->next){
                if(f3)
                    l3->val = l1->val + l2->val + flag;
                else
                    l3->val = l2->val + flag;
                l2 = l2->next;
                f3 = false;
                if(l3->val >= 10){
                    l3->val = l3->val % 10;
                    flag = 1;
                }
                else
                    flag = 0;
                l3->next = new ListNode(0);
                l3 = l3->next;
            }
            else if(!l2->next && !l1->next){
                //l3->val = 2;
                if(f3 && !f4)
                    l3->val = l1->val + flag;
                    if(l3->val >= 10){
                        l3->val = l3->val % 10;
                        l3->next = new ListNode(0);
                        l3 = l3->next;
                        l3->val = 1;
                }
                if(f4 && !f3)
                    l3->val = l2->val + flag;
                    if(l3->val >= 10){
                        l3->val = l3->val % 10;
                        l3->next = new ListNode(0);
                        l3 = l3->next;
                        l3->val = 1;
                }
                if(f4 && f3)
                    l3->val = l1->val + l2->val + flag;
                if(l3->val >= 10){
                    l3->val = l3->val % 10;
                    l3->next = new ListNode(0);
                    l3 = l3->next;
                    l3->val = 1;
                }
                break;
            }

        }
        return l4;
    }
};
