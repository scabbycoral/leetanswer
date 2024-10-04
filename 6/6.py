class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            #转折点
            i += flag
            print(res)
        return "".join(res)
#本题只需要N字形插入，不需要N形状中的空格，所以就是简单的从上到下从下到上来回插入