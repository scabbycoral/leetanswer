class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            postorder(root.left)
            
            postorder(root.right)
            
        
        res = list()
        postorder(root)
        return res
