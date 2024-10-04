class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        #？拿来判断空栈
        stack = ['?']
        #栈不能为空，如果第一个c就是右括号，则无法pop
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
            #如果出栈元素和
        return len(stack) == 1
