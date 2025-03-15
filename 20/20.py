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


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:  # s 长度必须是偶数
            return False
        mp = {'(': ')', '[': ']', '{': '}'}
        st = []
        for c in s:
            if c in mp:  # c 是左括号
                st.append(mp[c])  # 入栈对应的右括号
            elif not st or st.pop() != c:  # c 是右括号
                return False  # 没有左括号，或者左括号类型不对
        return not st  # 所有左括号必须匹配完毕


class Solution:
    def isValid(self, s: str) -> bool:
        dic={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if not stack or i in dic.values():
                stack.append(i)
            else:
                if stack[-1]==dic[i]:
                    stack.pop()
                else:
                    return False
        return not stack
        #为什么加not stack
        #因为False有两种情况，一种是左右括号不匹配，从return False退出
        #一种是stack已经清空了，但是进入了一个无法匹配的右括号，这样不管这个右括号右侧是否符合规则，到最后stack一定不是空的
        #如果i不是左括号，那么符合第一个if标准的情况一定是，i是右括号并且stack为空