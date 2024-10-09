class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        #？拿来判断空栈
        stack = ['?']
        #栈不能为空，如果第一个c就是右括号，则无法pop
        #因为下面的正常方法是先检测然后再pop，这个方法里是直接用pop进行检测，所以为了避免空栈需要一个额外元素
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
            #如果出栈元素和
        return len(stack) == 1

#下面这个方法更好理解
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    #如果stack空说明多了一个右括号，不匹配也返回false
                    return False
                else:
                #这个else可以不加
                    stack.pop()
            else:
                stack.append(ch)
        
        return not stack
