class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

假设有一个不是2的幂的数字符合 n&(n-1) == 0;
不是2的幂的数字一定满足如下条件: 要么是0, 要么二进制表示里不止一个1.
即可以表示成 x1x1x , x表示0个或者多个数字(可以是0, 也可以是1)
那么n-1 一定可以表示成 x1x, 则 n&(n-1) = x1x
所以 n&(n-1) == 0; 不成立.

结论若 n&(n-1) == 0 则 n为2的幂