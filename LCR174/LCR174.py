class Solution:
    def findTargetNode(self, root: TreeNode, cnt: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.cnt == 0: return
            self.cnt -= 1
            if self.cnt == 0: self.res = root.val
            dfs(root.left)

        self.cnt = cnt
        dfs(root)
        return self.res
#二叉搜索树的中序遍历是从小到大排列，所以需要正向dfs