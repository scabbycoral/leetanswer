class RBNode:
    """红黑树的节点类"""
    def __init__(self, key, color="RED", left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    """红黑树类"""
    def __init__(self):
        self.root = None  # 根节点初始化为 None

    def insert(self, key):
        """插入操作"""
        new_node = RBNode(key)  # 创建新节点，默认颜色为红色
        self._insert_node(new_node)  # 插入节点
        self._insert_fixup(new_node)  # 修复红黑树性质

    def _insert_node(self, node):
        """插入节点的辅助函数"""
        parent = None
        current = self.root
        while current is not None:  # 找到插入位置
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if parent is None:
            self.root = node  # 树为空，新节点为根节点
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        node.left = None  # 新节点的子节点为 None（叶子节点）
        node.right = None

    def _insert_fixup(self, node):
        """插入后修复红黑树性质"""
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "RED":
                    # Case 1: 叔叔节点是红色
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: 叔叔节点是黑色，且当前节点是右子节点
                        node = node.parent
                        self._left_rotate(node)
                    # Case 3: 叔叔节点是黑色，且当前节点是左子节点
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)
            else:
                # 对称情况
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "RED":
                    # Case 1: 叔叔节点是红色
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: 叔叔节点是黑色，且当前节点是左子节点
                        node = node.parent
                        self._right_rotate(node)
                    # Case 3: 叔叔节点是黑色，且当前节点是右子节点
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._left_rotate(node.parent.parent)
        self.root.color = "BLACK"  # 根节点始终为黑色

    def delete(self, key):
        """删除操作"""
        node = self.search(key)  # 找到要删除的节点
        if node is None:
            return  # 如果节点不存在，直接返回
        
        y = node  # y 是要删除的节点
        y_original_color = y.color  # 记录 y 的原始颜色

        if node.left is None:
            # 如果左子节点为空，用右子节点替换当前节点
            x = node.right
            self.transplant(node, node.right)
        elif node.right is None:
            # 如果右子节点为空，用左子节点替换当前节点
            x = node.left
            self.transplant(node, node.left)
        else:
            # 如果有两个子节点，找到右子树的最小节点
            y = self._find_min(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                # 如果 y 是 node 的直接右子节点
                if x is not None:
                    x.parent = y
            else:
                # 如果 y 不是 node 的直接右子节点
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            # 用 y 替换 node
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        # 如果 y 的原始颜色是黑色，修复红黑树性质
        if y_original_color == "BLACK":
            self._delete_fixup(x)

    def transplant(self, u, v):
        """用子树 v 替换子树 u"""
        if u.parent is None:
            self.root = v  # 如果 u 是根节点，直接将 v 设为根节点
        elif u == u.parent.left:
            u.parent.left = v  # 如果 u 是左子节点，用 v 替换 u
        else:
            u.parent.right = v  # 如果 u 是右子节点，用 v 替换 u
        if v is not None:
            v.parent = u.parent  # 更新 v 的父节点

    def _delete_fixup(self, x):
        """删除后修复红黑树性质"""
        while x != self.root and (x is None or x.color == "BLACK"):
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == "RED":
                    # Case 1: 兄弟节点是红色
                    sibling.color = "BLACK"
                    x.parent.color = "RED"
                    self._left_rotate(x.parent)
                    sibling = x.parent.right
                if (sibling.left is None or sibling.left.color == "BLACK") and \
                   (sibling.right is None or sibling.right.color == "BLACK"):
                    # Case 2: 兄弟节点是黑色，且兄弟节点的两个子节点都是黑色
                    sibling.color = "RED"
                    x = x.parent
                else:
                    if sibling.right is None or sibling.right.color == "BLACK":
                        # Case 3: 兄弟节点是黑色，且兄弟节点的左子节点是红色，右子节点是黑色
                        sibling.left.color = "BLACK"
                        sibling.color = "RED"
                        self._right_rotate(sibling)
                        sibling = x.parent.right
                    # Case 4: 兄弟节点是黑色，且兄弟节点的右子节点是红色
                    sibling.color = x.parent.color
                    x.parent.color = "BLACK"
                    sibling.right.color = "BLACK"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                # 对称情况
                sibling = x.parent.left
                if sibling.color == "RED":
                    # Case 1: 兄弟节点是红色
                    sibling.color = "BLACK"
                    x.parent.color = "RED"
                    self._right_rotate(x.parent)
                    sibling = x.parent.left
                if (sibling.right is None or sibling.right.color == "BLACK") and \
                   (sibling.left is None or sibling.left.color == "BLACK"):
                    # Case 2: 兄弟节点是黑色，且兄弟节点的两个子节点都是黑色
                    sibling.color = "RED"
                    x = x.parent
                else:
                    if sibling.left is None or sibling.left.color == "BLACK":
                        # Case 3: 兄弟节点是黑色，且兄弟节点的右子节点是红色，左子节点是黑色
                        sibling.right.color = "BLACK"
                        sibling.color = "RED"
                        self._left_rotate(sibling)
                        sibling = x.parent.left
                    # Case 4: 兄弟节点是黑色，且兄弟节点的左子节点是红色
                    sibling.color = x.parent.color
                    x.parent.color = "BLACK"
                    sibling.left.color = "BLACK"
                    self._right_rotate(x.parent)
                    x = self.root
        if x is not None:
            x.color = "BLACK"

    def _left_rotate(self, x):
        """左旋"""
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        """右旋"""
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

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

    def _find_min(self, node):
        """找到子树的最小节点"""
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        """中序遍历"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """递归中序遍历辅助函数"""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append((node.key, node.color))
            self._inorder_recursive(node.right, result)