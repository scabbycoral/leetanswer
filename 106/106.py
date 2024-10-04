def recur(in_start, in_end, post_start, root):
            if in_start > in_end or post_start > root:
                return None
            
            # The root value is the last element in the current postorder segment
            root_val = postorder[root]
            node = TreeNode(root_val)
            
            # Find the index of the root in the inorder segment
            i = hmap[root_val]
            
            # Number of nodes in the left subtree
            left_tree_size = i - in_start
            
            # Recursively build the left and right subtree
            node.left = recur(in_start, i - 1, post_start, post_start + left_tree_size - 1)
            node.right = recur(i + 1, in_end, post_start + left_tree_size, root - 1)
            
            return node
        
        # Build a hash map to quickly find index of values in inorder traversal
        hmap = {value: index for index, value in enumerate(inorder)}
        
        # Start recursion from the entire range of inorder and postorder lists
        return recur(0, len(inorder) - 1, 0, len(postorder) - 1)
