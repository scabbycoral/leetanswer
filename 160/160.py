# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#如果没有共同节点则相交于None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A=headA
        B=headB
        while A!=B:
            A=A.next if A else headB
            #因为换边的时候A是None，所以判断的是A而不是A.next
            #注意if A说明A到了末尾还会向None走一步
            B=B.next if B else headA
            #位置长度一样，则一直next就能找到
            #如果位置长度不一样，则遍历当前列表结束后换另一个继续遍历
            #当A先遍历A再遍历B，找到节点c的步数为，a+b-c
            #B也是同样，所以在b+a-c一定可以找到c，所以同时遍历就可以
            #如果没有相交节点，则相交于None
        return A