# Python file for number 质数因子 
import sys

for line in sys.stdin:
    a = line.strip()
    def prime_factors(n):
        factors = []
        # 处理 2 的因子
        #一直除以2
        while n % 2 == 0:
            print(2,end=" ")
            factors.append(2)
            n //= 2
        # 处理奇数因子
        divisor = 3
        while divisor * divisor <= n:
            while n % divisor == 0:
                print(divisor,end=" ")
                factors.append(divisor)
                n //= divisor
            divisor += 2
        # 如果 n 是质数，且无法被拆
        if n > 2:
            print(n,end=" ")
            factors.append(n)
        return factors
    prime_factors(int(a))
    #print(prime_factors(int(a)))