class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1
#queue1需要top的元素留在queue1，其余元素转移到queue2，然后queue1top这个元素，再将其余元素转移回来