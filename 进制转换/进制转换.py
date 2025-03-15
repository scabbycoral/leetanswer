# Python file for number 进制转换 
def to_decimal(number, base):
    """
    将任意进制的数转换为十进制数。

    :param number: 要转换的数（字符串形式）
    :param base: 原始进制（整数，范围 2-36）
    :return: 转换后的十进制数（整数）
    """
    # 定义字符集，用于表示 0-9 和 a-z
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"

    # 检查进制范围是否合法
    if base < 2 or base > 36:
        raise ValueError("进制范围必须在 2 到 36 之间")

    # 检查输入是否为空
    if not number:
        return 0

    # 去掉前缀（如 0x, 0b, 0o）
    if number.startswith("0x") or number.startswith("0X"):
        if base != 16:
            raise ValueError("前缀 0x 或 0X 表示十六进制，但输入的进制不匹配")
        number = number[2:]
    elif number.startswith("0b") or number.startswith("0B"):
        if base != 2:
            raise ValueError("前缀 0b 或 0B 表示二进制，但输入的进制不匹配")
        number = number[2:]
    elif number.startswith("0o") or number.startswith("0O"):
        if base != 8:
            raise ValueError("前缀 0o 或 0O 表示八进制，但输入的进制不匹配")
        number = number[2:]

    decimal_number = 0

    # 遍历每一位
    for i, char in enumerate(reversed(number)):
        if char.isdigit():
            value = int(char)
        elif char.lower() in chars[10:base]:
            value = ord(char.lower()) - ord('a') + 10
        else:
            raise ValueError(f"非法字符 '{char}'，请输入合法的 {base} 进制数")

        # 检查值是否合法
        if value >= base:
            raise ValueError(f"字符 '{char}' 在 {base} 进制中无效")

        decimal_number += value * (base ** i)

    return decimal_number
    
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n:
            res += n % k
            n //= k
        return res
