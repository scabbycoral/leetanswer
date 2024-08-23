# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val==val:return head.next
        #头节点就是
        pre,cur=head,head.next
        while cur and cur.val!=val:
            pre,cur=cur,pre.next
        if cur:
            pre.next=cur.next
        #非头节点
        return head