#本题目的是用所给的资源构造回文串，而不是寻找回文串

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res, record = 0, set()
        for c in s:
            if c in record:
                res+=2
                record.remove(c)
            else:
                record.add(c)
        return res+1 if record else res
#消消乐，遇到重复的就把这两个都删除，res+2
#本题默认只有一个回文串

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 统计各字符数量
        counter = collections.defaultdict(int)
        for c in s:
            counter[c] += 1
        res, odd = 0, 0
        # 统计构造回文串的最大长度
        for count in counter.values():
            # 将当前字符出现次数向下取偶数，并计入 res
            rem = count % 2
            res += count - rem
            # 若当前字符出现次数为奇数，则将 odd 置 1
            if rem == 1: odd = 1
        return res + odd
