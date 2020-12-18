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
        ListNode* tar = new ListNode();
		ListNode* tar1 = new ListNode();
		ListNode* tar2 = new ListNode();
		tar1 = tar;
		int temp = 0;
		if (l1 || l2) {
			while (l1 && l2) {
				ListNode* l3 = new ListNode((l1->val + l2->val + temp) % 10);
				
				tar->next = l3;
				if ((l1->val + l2->val + temp) >= 10) {
					temp = 1;
				}
                else
                    temp = 0;
				l1 = l1->next;
				l2 = l2->next;
				tar = tar->next;
			}
			tar2 = tar1->next;
			while (l1 || l2) {
				if (l1) {
					while (l1) {
						ListNode* l4 = new ListNode((l1->val + temp) % 10);
						
						if ((l1->val + temp) >= 10) {
							temp = 1;
						}
						else
							temp = 0;
						tar->next = l4;
						l1 = l1->next;
						tar = tar->next;
					}
				}
				if (l2) {
					while (l2) {
						ListNode* l5 = new ListNode((l2->val + temp) % 10);
						
						if ((l2->val + temp) >= 10) {
							temp = 1;
						}
						else
							temp = 0;
						tar->next = l5;
						l2 = l2->next;
						tar = tar->next;
					}
				}
			}
			//if (!(l1 && l2) && (temp == 1)) {
            if (temp == 1) {
				ListNode* l7 = new ListNode(1);
				tar->next = l7;
			}
		}
		return tar2;
    }
};
