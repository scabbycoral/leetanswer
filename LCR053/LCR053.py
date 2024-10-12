# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        #如果右子树不空，则后继是右子树里最小值
        if p.right:
            q=p.right
            while q.left:
                q=q.left
            return q
        r=None
        #否则是父节点
        while root:
            if root.val<p.val:
                root=root.right
            elif root.val>p.val:
                r=root
                root=root.left
            else:return r