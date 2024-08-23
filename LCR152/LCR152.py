class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            #记录左子树区间
            while postorder[p] > postorder[j]: p += 1
            #记录右子树区间
            return p == j and recur(i, m - 1) and recur(m, j - 1)
            #p==j判断是否是二叉搜索树后序遍历

        return recur(0, len(postorder) - 1)
