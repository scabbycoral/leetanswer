# Python file for number 443 
#



#原地压缩
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        write = 0
        while i < n:
            j = i
            #找到最后一个和i位置相似的元素位置
            while j < n and chars[j] == chars[i]:
                j += 1
                
            chars[write] = chars[i]
            write += 1
            if j - i > 1:
                for c in str(j-i):
                    chars[write] = c
                    write += 1
            i = j
        return write
