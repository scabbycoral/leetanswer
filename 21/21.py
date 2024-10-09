class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dum = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
            cur = cur.next
            #注意指针后移
        cur.next = list1 if list1 else list2
        return dum.next
        #创建新链表


#递归
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 not None:
            return list2
        elif list2 not None:
            return list1
        elif list2.val>list1.val:
            list1.next=mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next=mergeTwoLists(list1,list2.next)
            return list2
            #如果不需要插入就会一直next
            #不创建新链表
            
        
        
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
        #把上面的四个if缩减成两个if，因为左面是l1还是l2无所谓，找到需要插入的就交换l1l2
        
#可读性优化
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 如果其中一个链表为 None，返回另一个链表
        if not list1:
            return list2
        if not list2:
            return list1
        
        # 确保 list1 是较小值的节点
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        # 递归调用，合并 list1 的下一个节点和 list2
        list1.next = self.mergeTwoLists(list1.next, list2)
        
        return list1  # 返回以 list1 为开头的合并链表