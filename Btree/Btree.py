# Python file for number Btree 
class BTreeNode:
    """B 树的节点类"""
    def __init__(self, t, leaf=False):
        self.t = t  # 最小度数
        self.keys = []  # 节点的键
        self.children = []  # 节点的子节点
        self.leaf = leaf  # 是否为叶子节点

    def __str__(self):
        return f"Keys: {self.keys}, Leaf: {self.leaf}"
        
class BTree:
    """B 树类"""
    def __init__(self, t):
        self.t = t  # 最小度数
        self.root = BTreeNode(t, leaf=True)  # 根节点初始化为叶子节点

    def search(self, key):
        """查找操作"""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """递归查找辅助函数"""
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node, i  # 找到键
        if node.leaf:
            return None  # 未找到键
        return self._search_recursive(node.children[i], key)

    def insert(self, key):
        """插入操作"""
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            # 如果根节点已满，分裂根节点
            new_root = BTreeNode(self.t, leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        """在非满节点中插入键"""
        i = len(node.keys) - 1
        if node.leaf:
            # 如果是叶子节点，直接插入
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # 如果不是叶子节点，找到合适的子节点
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                # 如果子节点已满，分裂子节点
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, index):
        """分裂子节点"""
        t = self.t
        child = parent.children[index]
        new_child = BTreeNode(t, leaf=child.leaf)

        # 将 child 的键和子节点分成两部分
        parent.keys.insert(index, child.keys[t - 1])
        parent.children.insert(index + 1, new_child)

        new_child.keys = child.keys[t:(2 * t - 1)]
        child.keys = child.keys[0:(t - 1)]

        if not child.leaf:
            new_child.children = child.children[t:(2 * t)]
            child.children = child.children[0:t]

    def delete(self, key):
        """删除操作"""
        self._delete_recursive(self.root, key)
        if len(self.root.keys) == 0:
            # 如果根节点没有键，将子节点设为新的根节点
            if not self.root.leaf:
                self.root = self.root.children[0]
            else:
                self.root = None

    def _delete_recursive(self, node, key):
        """递归删除辅助函数"""
        t = self.t
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            # 找到键
            if node.leaf:
                # 如果是叶子节点，直接删除
                node.keys.pop(i)
            else:
                # 如果不是叶子节点，处理内部节点
                self._delete_internal_node(node, i)
        else:
            if node.leaf:
                # 未找到键
                return
            # 递归删除子节点
            if len(node.children[i].keys) < t:
                # 如果子节点键不足，需要调整
                self._fix_child(node, i)
                if i > len(node.keys):
                    i -= 1
            self._delete_recursive(node.children[i], key)

    def _delete_internal_node(self, node, index):
        """删除内部节点的键"""
        t = self.t
        key = node.keys[index]

        if len(node.children[index].keys) >= t:
            # 如果左子节点键足够，找到前驱
            predecessor = self._get_predecessor(node.children[index])
            node.keys[index] = predecessor
            self._delete_recursive(node.children[index], predecessor)
        elif len(node.children[index + 1].keys) >= t:
            # 如果右子节点键足够，找到后继
            successor = self._get_successor(node.children[index + 1])
            node.keys[index] = successor
            self._delete_recursive(node.children[index + 1], successor)
        else:
            # 如果左右子节点键都不足，合并子节点
            self._merge_children(node, index)
            self._delete_recursive(node.children[index], key)

    def _get_predecessor(self, node):
        """找到前驱"""
        while not node.leaf:
            node = node.children[-1]
        return node.keys[-1]

    def _get_successor(self, node):
        """找到后继"""
        while not node.leaf:
            node = node.children[0]
        return node.keys[0]

    def _fix_child(self, parent, index):
        """调整子节点"""
        t = self.t
        if index > 0 and len(parent.children[index - 1].keys) >= t:
            # 从左兄弟节点借一个键
            self._borrow_from_left(parent, index)
        elif index < len(parent.children) - 1 and len(parent.children[index + 1].keys) >= t:
            # 从右兄弟节点借一个键
            self._borrow_from_right(parent, index)
        else:
            # 合并子节点
            if index < len(parent.children) - 1:
                self._merge_children(parent, index)
            else:
                self._merge_children(parent, index - 1)

    def _borrow_from_left(self, parent, index):
        """从左兄弟节点借一个键"""
        child = parent.children[index]
        left_sibling = parent.children[index - 1]

        child.keys.insert(0, parent.keys[index - 1])
        parent.keys[index - 1] = left_sibling.keys.pop()

        if not child.leaf:
            child.children.insert(0, left_sibling.children.pop())

    def _borrow_from_right(self, parent, index):
        """从右兄弟节点借一个键"""
        child = parent.children[index]
        right_sibling = parent.children[index + 1]

        child.keys.append(parent.keys[index])
        parent.keys[index] = right_sibling.keys.pop(0)

        if not child.leaf:
            child.children.append(right_sibling.children.pop(0))

    def _merge_children(self, parent, index):
        """合并子节点"""
        t = self.t
        child = parent.children[index]
        sibling = parent.children[index + 1]

        child.keys.append(parent.keys.pop(index))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        parent.children.pop(index + 1)

    def inorder_traversal(self):
        """中序遍历"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """递归中序遍历辅助函数"""
        if node:
            for i in range(len(node.keys)):
                if not node.leaf:
                    self._inorder_recursive(node.children[i], result)
                result.append(node.keys[i])
            if not node.leaf:
                self._inorder_recursive(node.children[-1], result)