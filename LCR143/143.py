class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: 
                return True
            if not A or A.val != B.val: 
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
#isSubStructure表示从哪个节点开始当根节点
#recur表示从这个节点开始检测子结构

#有一种情况是a没遍历结束但是b结束了，说明b全部出现在a内但是不拥有相同的叶子节点