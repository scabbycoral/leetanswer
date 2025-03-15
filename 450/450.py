

#算法导论版，带parent指针
class TreeNode:
    """二叉搜索树的节点类"""
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent  # 父节点指针

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = self.search(root, key)  # 找到要删除的节点
        if node is None:
            return root  # 如果节点不存在，直接返回
        
        if node.left is None:
            # 只有右子节点，用右子节点替换当前节点
            root = self.transplant(root, node, node.right)
        elif node.right is None:
            # 只有左子节点，用左子节点替换当前节点
            root = self.transplant(root, node, node.left)
        else:
            # 有两个子节点，找到右子树的最小节点
            min_node = self._find_min(node.right)
            if min_node.parent != node:
                # 如果最小节点不是 node 的直接右子节点
                root = self.transplant(root, min_node, min_node.right)
                min_node.right = node.right
                min_node.right.parent = min_node
            # 用最小节点替换当前节点
            root = self.transplant(root, node, min_node)
            min_node.left = node.left
            min_node.left.parent = min_node
        return root

    def transplant(self, root: TreeNode, u: TreeNode, v: Optional[TreeNode]) -> TreeNode:
        """用子树 v 替换子树 u"""
        if u.parent is None:
            # 如果 u 是根节点，直接将 v 设为根节点
            root = v
        elif u == u.parent.left:
            # 如果 u 是左子节点，用 v 替换 u
            u.parent.left = v
        else:
            # 如果 u 是右子节点，用 v 替换 u
            u.parent.right = v
        if v is not None:
            # 更新 v 的父节点
            v.parent = u.parent
        return root

        
#递归，不带parent指针
def delete(self, key):
    """删除操作"""
    self.root = self._delete_recursive(self.root, key)

def _delete_recursive(self, node, key):
    """递归删除辅助函数"""
    if node is None:
        return node  # 节点不存在，直接返回

    # 找到要删除的节点
    if key < node.key:
        node.left = self._delete_recursive(node.left, key)
    elif key > node.key:
        node.right = self._delete_recursive(node.right, key)
    else:
        # 找到要删除的节点
        if node.left is None:
            return node.right  # 只有右子节点
        elif node.right is None:
            return node.left  # 只有左子节点
        else:
            # 有两个子节点，找到右子树的最小节点
            min_node = self._find_min(node.right)
            node.key = min_node.key  # 用最小节点的值替换当前节点
            node.right = self._delete_recursive(node.right, min_node.key)  # 删除右子树的最小节点
    return node