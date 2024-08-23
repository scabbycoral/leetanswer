# 不考虑大数越界问题，带剪枝，原来的递归有冗余计算
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
