#LCR123是新解法
#递归先后指针
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre     # 终止条件
            res = recur(cur.next, cur) # 递归后继节点
            #pre入参为cur代替了pre=cur
            #用传参代替了134
            cur.next = pre             # 修改节点引用指向
            #第二步不变
            return res                 # 返回反转链表的头节点
        
        return recur(head, None)       # 调用递归并返回
#res是为了找尾节点当返回值，cur.next=pre是在回程的时候转置
#这里不赋值None是因为pre是上一步的cur，上一层的cur.next=pre就已经代替了赋值None
#head需要是因为变成上一层就取不到当前的head了，无法通过head.next.next=head修改
#空间复杂度O(n)
#从cur指向pre

#单节点递归
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head
        #not head.next是说存在末尾节点并到达末尾节点的情况
        #not head是head空链表的情况，只此一种
        res=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return res
#将cur的下一个节点的next指向cur，并且将cur的next指向None避免产生环
#其余的操作都是转置，逻辑和上面的一样但是更好理解

#先后指针迭代
#tmp保存需要转置的下一个节点
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next # 暂存后继节点 cur.next#1
            cur.next = pre # 修改 next 引用指向#2
            pre = cur      # pre 暂存 cur#3
            cur = tmp      # cur 访问下一节点#4
            #第二步是重定向，第134步是把cur和pre后移一位
        return pre
#从头到尾，依次逆向，尾节点是null，null指向头节点，头节点指向第二个节点
#pre保存cur之前的节点，cur通过"=tmp"依次后移
#链表逆置分四步

#先后指针迭代
#tmp保存需要转置的节点
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur,pre=head,None
        while cur:
            tmp=cur
            cur=cur.next
            tmp.next=pre
            pre=tmp
        return pre