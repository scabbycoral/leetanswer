# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=pre=head
        while cur:
            if cur.next:
                cur=cur.next.next
                pre=pre.next
            else:
                return pre
            if not cur:
                return pre
#更好理解的方式
                
                
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
        #满足这两个条件才能找到next.next
            fast = fast.next.next
            slow = slow.next
        return slow

#或者存到数组或者字典里，遍历得到结果