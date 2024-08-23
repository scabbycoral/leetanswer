class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        slow, fast, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        
        pre.next = pre.next.next
        #删除，pre在中间
        return head
#快慢指针找中间节点