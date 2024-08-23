class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        return self.reverseBookList(head.next) + [head.val] if head else []


class Solution:
    def reverseBookList(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
