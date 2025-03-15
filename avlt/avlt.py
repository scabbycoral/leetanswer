# Python file for number avlt 
class AVLNode:
    """AVL 树的节点类"""
    def __init__(self, key):
        self.key = key  # 节点值
        self.height = 1  # 节点高度
        self.left = None  # 左子节点
        self.right = None  # 右子节点
        
class AVLTree:
    """AVL 树类"""
    def __init__(self):
        self.root = None  # 根节点初始化为 None

    def insert(self, key):
        """插入操作"""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        """递归插入辅助函数"""
        if node is None:
            return AVLNode(key)  # 创建新节点
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            return node  # 重复值不插入

        # 更新节点高度
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # 修复平衡
        #node是父节点
        return self._fix_balance(node, key)

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

        # 更新节点高度
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # 修复平衡
        return self._fix_balance(node, key)

    def _fix_balance(self, node, key):
        """修复平衡"""
        balance = self._get_balance(node)

        # 左子树不平衡
        if balance > 1:
            if key < node.left.key:
                # 左左情况，右旋
                return self._right_rotate(node)
            else:
                # 左右情况，先左旋再右旋
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        # 右子树不平衡
        if balance < -1:
            if key > node.right.key:
                # 右右情况，左旋
                return self._left_rotate(node)
            else:
                # 右左情况，先右旋再左旋
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        """左旋"""
        y = z.right
        T2 = y.left

        # 执行旋转
        y.left = z
        z.right = T2

        # 更新高度
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        """右旋"""
        y = z.left
        T3 = y.right

        # 执行旋转
        y.right = z
        z.left = T3

        # 更新高度
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        """获取节点高度"""
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        """获取平衡因子"""
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _find_min(self, node):
        """找到子树的最小节点"""
        while node.left is not None:
            node = node.left
        return node

    def search(self, key):
        """查找操作"""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """递归查找辅助函数"""
        if node is None or key == node.key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """中序遍历"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """递归中序遍历辅助函数"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)