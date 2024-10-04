# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag=0
        head=res=ListNode()
        while l1 or l2 or flag:
        #注意这个flag
            num=(l1.val if l1 else 0) +(l2.val if l2 else 0) +flag
            res.next=ListNode(num%10)
            flag=num//10
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

            res=res.next
        
        
        return head.next

