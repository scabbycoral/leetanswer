#可以用236的解
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        #上面两种情况都是qp位于同侧，说明root不是根节点，如果root是最小父节点说明左子树是q右子树是p
        
        #如果不符合两种情况说明找到了一个是qp根的root
        return root
