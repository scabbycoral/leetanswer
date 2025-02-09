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

#可读性更好
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # Helper function to check if tree B is a substructure of tree A
        def isMatch(A: TreeNode, B: TreeNode) -> bool:
            if not B:
                return True  # An empty tree B is always a substructure
            if not A or A.val != B.val:
                return False  # A must match B's root value
            # Recursively check left and right subtrees
            return isMatch(A.left, B.left) and isMatch(A.right, B.right)
        
        # If either tree A or B is None, B cannot be a substructure of A
        if not A or not B:
            return False
        
        # Check if B is a substructure of A starting at the root of A
        return (
            isMatch(A, B) or 
            self.isSubStructure(A.left, B) or 
            self.isSubStructure(A.right, B)
        )
        #return的顺序