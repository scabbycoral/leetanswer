class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        # 循环，当进位为 0 时跳出
        while b != 0:
            # a, b = 非进位和, 进位
            a, b = (a ^ b), (a & b) << 1 & x
            #循环是因为即使计算出来进位和原位，依旧需要加法
            #所以将以前的ab换成进位和原位，直到进位为0，说明原位就是进位+原位的结果，也就是最初加法的结果
        return a if a <= 0x7fffffff else ~(a ^ x)
