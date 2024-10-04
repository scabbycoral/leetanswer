class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1: 
                res *= x
            #结算，每当1位进行一次，"从后到前"，中间的位0只进行x的n次方运算
            #比如1001，先计算res1，然后00的x累乘，然后res1第二个，将res1和00的x累乘相乘
            x *= x
            #x*x是为了一直取计算下一位的值，具体要不要用到要看n&1
            n >>= 1
        return res
