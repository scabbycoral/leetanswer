class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.left)
            #一直left走，直到最小
            if self.k == 0: return
            self.k -= 1
            #从小到大递减k，直到k为0找到目标
            if self.k == 0: self.res = root.val
            dfs(root.right)

        self.k = k
        dfs(root)
        return self.res
#二叉搜索树的中序遍历是从小到大排列，所以需要逆向向dfs