#插入排序
#因为本题的第一个节点就有可能被移动，所以返回head没有意义，head有可能已经成为别的节点，需要一个虚拟节点在函数一开始就指向head
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(-1)
        #res.next=head
        #不能连上，因为不知道head会指向那里
        key=head
        while key:
            tmp=key.next
            #1.1记录key取出位置
            pre=res
            while pre.next and pre.next.val<key.val:
                pre=pre.next
            key.next=pre.next
            pre.next=key
            #2.合适位置插入，pre.next
            #res初始时后面是没有节点的，通过pre.next不断连接转移的节点
            key=tmp
            #1.2将取出key位置的空缺连上
        return res.next

#归并排序