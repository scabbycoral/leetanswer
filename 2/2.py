# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)
        #l4 = ListNode(None)
        l4 = l3
        flag = 0
        while l1 or l2 or flag:
            flag += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            l3.next = ListNode(flag%10)
            flag //= 10
            l3 = l3.next
            #l1 = l1.next if l1 else None
            #l2 = l2.next if l2 else None
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        return l4.next
