# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        # 否则，递归地遍历树
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        y=None
        x=root
        while x:
            y=x
            if x.val>val:x=x.left
            elif x.val<val:x=x.right
            else:return root
        z=TreeNode(val)
        if z.val<y.val:y.left=z
        elif:y.right=z
        return root
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)  # 如果树为空，直接插入为根节点
        else:
            self._insert_recursive(root, val)
        return root

    def _insert_recursive(self, node, val):
        """递归插入辅助函数"""
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)  # 插入到左子树
            else:
                self._insert_recursive(node.left, val)
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val)  # 插入到右子树
            else:
                self._insert_recursive(node.right, val)