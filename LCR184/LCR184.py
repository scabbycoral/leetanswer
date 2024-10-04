import queue

class Checkout:
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()
        #deque用来get_max

    def get_max(self) -> int:
        return self.deque[0] if self.deque else -1

    def add(self, value: int) -> None:
        self.queue.put(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
            #deque只保存不小于x的元素，递减
        self.deque.append(value)

    def remove(self) -> int:
        if self.queue.empty(): return -1
        val = self.queue.get()
        if val == self.deque[0]:
            self.deque.popleft()
            #如果没进到这个if里说明val比deque里最小值小，已经pop了
        return val
