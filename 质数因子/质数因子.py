# Python file for number �������� 
import sys

for line in sys.stdin:
    a = line.strip()
    def prime_factors(n):
        factors = []
        # ���� 2 ������
        #һֱ����2
        while n % 2 == 0:
            print(2,end=" ")
            factors.append(2)
            n //= 2
        # ������������
        divisor = 3
        while divisor * divisor <= n:
            while n % divisor == 0:
                print(divisor,end=" ")
                factors.append(divisor)
                n //= divisor
            divisor += 2
        # ��� n �����������޷�����
        if n > 2:
            print(n,end=" ")
            factors.append(n)
        return factors
    prime_factors(int(a))
    #print(prime_factors(int(a)))