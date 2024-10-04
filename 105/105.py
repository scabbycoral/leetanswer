class Solution:
    def deduceTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
        #root从pre中来
        #i，l，r从in中来
        #l，r都是为了计算root，不会直接使用，直接使用的只有root
            if left > right: return                               # 递归终止
            node = TreeNode(preorder[root])                       # 建立根节点
            #preorder[root]是指当前root节点在先序中的值
            i = hmap[preorder[root]]                              # 从中序遍历找到划分根节点位置，从先序找到根节点值
            node.left = recur(root + 1, left, i - 1)              # 开启左子树递归
            #注意区分root和i
            node.right = recur(i - left + root + 1, i + 1, right) # 开启右子树递归
            return node                                           # 回溯返回根节点

        hmap, preorder = {}, preorder
        for i in range(len(inorder)):
            hmap[inorder[i]] = i
            #存入哈希表为了更快找到下标，key是值，value是下标
        return recur(0, 0, len(inorder) - 1)
"""
def recur(root, in_start, in_end):
            if in_start > in_end:
                return None
            
            # The current root is the first element in preorder
            root_val = preorder[root]
            root = TreeNode(root_val)
            
            # Find the index of the root in inorder
            i = hmap[root_val]
            
            # Number of nodes in the left subtree
            left_tree_size = i - in_start
            
            # Recursively build the left and right subtree
            root.left = recur(root + 1, in_start, i - 1)
            root.right = recur(root + 1 + left_tree_size, i + 1, in_end)
            
            return root
        
        hmap = {value: index for index, value in enumerate(inorder)}
        
        return recur(0, 0, len(inorder) - 1)
"""