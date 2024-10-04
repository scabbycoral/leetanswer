class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
        #while True用来代替do while
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
