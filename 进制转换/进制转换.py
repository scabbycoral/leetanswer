# Python file for number ����ת�� 
def to_decimal(number, base):
    """
    ��������Ƶ���ת��Ϊʮ��������

    :param number: Ҫת���������ַ�����ʽ��
    :param base: ԭʼ���ƣ���������Χ 2-36��
    :return: ת�����ʮ��������������
    """
    # �����ַ��������ڱ�ʾ 0-9 �� a-z
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"

    # �����Ʒ�Χ�Ƿ�Ϸ�
    if base < 2 or base > 36:
        raise ValueError("���Ʒ�Χ������ 2 �� 36 ֮��")

    # ��������Ƿ�Ϊ��
    if not number:
        return 0

    # ȥ��ǰ׺���� 0x, 0b, 0o��
    if number.startswith("0x") or number.startswith("0X"):
        if base != 16:
            raise ValueError("ǰ׺ 0x �� 0X ��ʾʮ�����ƣ�������Ľ��Ʋ�ƥ��")
        number = number[2:]
    elif number.startswith("0b") or number.startswith("0B"):
        if base != 2:
            raise ValueError("ǰ׺ 0b �� 0B ��ʾ�����ƣ�������Ľ��Ʋ�ƥ��")
        number = number[2:]
    elif number.startswith("0o") or number.startswith("0O"):
        if base != 8:
            raise ValueError("ǰ׺ 0o �� 0O ��ʾ�˽��ƣ�������Ľ��Ʋ�ƥ��")
        number = number[2:]

    decimal_number = 0

    # ����ÿһλ
    for i, char in enumerate(reversed(number)):
        if char.isdigit():
            value = int(char)
        elif char.lower() in chars[10:base]:
            value = ord(char.lower()) - ord('a') + 10
        else:
            raise ValueError(f"�Ƿ��ַ� '{char}'��������Ϸ��� {base} ������")

        # ���ֵ�Ƿ�Ϸ�
        if value >= base:
            raise ValueError(f"�ַ� '{char}' �� {base} ��������Ч")

        decimal_number += value * (base ** i)

    return decimal_number
    
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n:
            res += n % k
            n //= k
        return res
