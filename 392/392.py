class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        i = 0
        for c in t:
            if s[i] == c:
                i += 1
                # 若已经遍历完 s ，则提前返回 true
                if i == len(s):
                    return True
        return False
#本题判断子串可以是不连着的，只要全部按顺序出现即可，中间可以断开
#双指针可以在同一个结构上，也可以在不同的结构上