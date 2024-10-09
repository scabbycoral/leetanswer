#双指针但全指向头
#本解法不需要额外空间
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        node=ListNode(0)
        node.next=head
        res=pre=cur=node
        #比x小的直接从链表头进入，记录头的位置，每转移过来一个节点，头节点就后移一位，为了保证原有的链表顺序
        while cur.next:
            if cur.next.val>=x:
                cur=cur.next
            else:
                temp=cur.next
                cur.next=cur.next.next
                temp.next=pre.next#连接后边
                pre.next=temp#连接前边
                pre=pre.next
                if cur.next==pre:
                #当原地交换，2134以3为基准交换2时
                #因为pre开始是0，经过上面的pre.next，已经变成了已经交换过后的一段的最后一个，cur.next是当时交换的节点位置，如果这两个位置的元素一样则说明是原地交换，需要cur去到next，否则会死循环
                    cur=cur.next
                #上面else里的逻辑不需要总进行cur=cur.next，因为如果cur.next被转移到前面，则下一个cur.next已经被重定向，必须要再次进行判断
        return res.next
#本题是链表重排序


#也可以将两种标准放到两个新的结构里，然后拼接

#题目要求小的在大的之前即可，所以不考虑组内顺序