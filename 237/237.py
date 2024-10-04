class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
#虽然node需要删除，但是删除的是node下一个节点，将下一个节点的信息转移到node上
#无法删除尾节点