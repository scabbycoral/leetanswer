class MinStack:
    def __init__(self):
        self.stack = []
        #用来保存push、pop顺序
        self.min_stack = []
        #用来保存逆序
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]: 
        #如果空或者更小
            self.min_stack.append(x)
    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
        #如果栈顶元素等于最小栈最后一个元素，说明栈右侧所有元素都大于栈顶元素，所以最小站中只有一个元素
            self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]
