class Solution {
public:
    vector<int> reverseBookList(ListNode* head) {
        recur(head);
        return res;
    }
private:
    vector<int> res;
    void recur(ListNode* head) {
        if(head == nullptr) return;
        recur(head->next);
        res.push_back(head->val);
    }
};


class Solution {
public:
    vector<int> reverseBookList(ListNode* head) {
        stack<int> stk;
        while(head != nullptr) {
            stk.push(head->val);
            head = head->next;
        }
        vector<int> res;
        while(!stk.empty()) {
            res.push_back(stk.top());
            stk.pop();
        }
        return res;
    }
};
