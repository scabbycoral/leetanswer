class Solution:
    def reverseMessage(self, message: str) -> str:
        message = message.strip()                      # 删除首尾空格
        i = j = len(message) - 1
        res = []
        while i >= 0:
            while i >= 0 and message[i] != ' ': i -= 1 # 搜索首个空格
            res.append(message[i + 1: j + 1])          # 添加单词
            while i >= 0 and message[i] == ' ': i -= 1 # 跳过单词间空格
            j = i                                      # j 指向下个单词的尾字符
        return ' '.join(res)                           # 拼接并返回
