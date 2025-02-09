class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
        #在同级别层不会直接进行root=successor，而是把surressor返回作为上一层的root.left或者root.right
            successor = root.right
            while successor.left:
                successor = successor.left
            successor.right = self.deleteNode(root.right, successor.val)
            successor.left = root.left
            return successor
        return root
#不要和transplant穿插，会出问题


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        cur, curParent = root, None
        while cur and cur.val != key:
            curParent = cur
            cur = cur.left if cur.val > key else cur.right
        if cur is None:
            return root
        if cur.left is None and cur.right is None:
            cur = None
        elif cur.right is None:
            cur = cur.left
        elif cur.left is None:
            cur = cur.right
        else:
            successor, successorParent = cur.right, cur
            while successor.left:
                successorParent = successor
                successor = successor.left
            if successorParent.val == cur.val:
                successorParent.right = successor.right
            else:
                successorParent.left = successor.right
            successor.right = cur.right
            successor.left = cur.left
            cur = successor
        if curParent is None:
            return cur
        if curParent.left and curParent.left.val == key:
            curParent.left = cur
        else:
            curParent.right = cur
        return root
