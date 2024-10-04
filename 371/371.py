class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        #补码补齐
        # 循环，当进位为 0 时跳出
        while b != 0:
            # a, b = 非进位和, 进位
            #a, b = (a ^ b), (a & b) << 1 & x
            sum=a^b
            carry=(a&b)<<1&x
            a=sum
            b=carry
            #第一次计算到这里时，已经和原本的ab没关系了，将ab加法转化为了进位和不进位数字的加法
        return a if a <= 0x7fffffff else ~(a ^ x)
#~(a^x)负数还原