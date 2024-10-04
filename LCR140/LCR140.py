class Solution:
    def trainingPlan(self, head: ListNode, cnt: int) -> ListNode:
        former, latter = head, head
        for _ in range(cnt):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter