class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        #dfs后序遍历
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        """
        #bfs
        if not root: return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res

