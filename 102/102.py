class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
        #遍历父节点
            tmp = []
            for _ in range(len(queue)):
            #单独加一个循环是为了整理到另一个list里，如果输出都在同一个list则代码为LCR149
                node = queue.popleft()
                #出当前父节点
                tmp.append(node.val)
                #当前层
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                #左右子树进入queue
            res.append(tmp)
        return res
