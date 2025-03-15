class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
        #while True用来代替do while
        #因为fast和slow一开始是一样的，所以没法用fast！=slow
        #结束条件在break的if这里
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
        #第一轮相遇找环，第二轮相遇找入口
        #或者将slow继续循环，查看回到原位这个环有多少个元素，然后再启动fast从头开始

#优化
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head  # 初始化快慢指针
        while fast and fast.next:  # 当 fast 和 fast.next 不为空时继续
            fast = fast.next.next  # 快指针移动两步
            slow = slow.next       # 慢指针移动一步
            if fast == slow:       # 如果快慢指针相遇，说明有环
                fast = head        # 将快指针重新指向链表头
                while fast != slow:  # 快慢指针同时移动，直到相遇
                    fast, slow = fast.next, slow.next
                return fast  # 返回环的起始节点
        return None  # 如果无环，返回 None