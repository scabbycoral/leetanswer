class Solution:
    def pathEncryption(self, path: str) -> str:
        res = []
        for c in path:
            if c == '.': res.append(' ')
            else: res.append(c)
        return "".join(res)

#空间复杂度无法降到O(1)，因为python字符串是不可变，只要有修改就一定是创建了新对象
