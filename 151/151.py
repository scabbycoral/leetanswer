class Solution:
    def reverseMessage(self, message: str) -> str:
        message = message.strip()                      # 删除首尾空格
        i = j = len(message) - 1
        res = []
        while i >= 0:
        #这个循环表示ji再次到了单词开头
            while i >= 0 and message[i] != ' ': i -= 1 # 搜索首个空格，i是单词后第一个空格的位置
            res.append(message[i + 1: j + 1])          # 添加单词
            while i >= 0 and message[i] == ' ': i -= 1 # 跳过单词间空格，i是空格后第一个字母的位置
            j = i                                      # j 指向下个单词的尾字符
        return ' '.join(res)                           # 拼接并返回
#i>=0是因为负数会从后往前继续循环