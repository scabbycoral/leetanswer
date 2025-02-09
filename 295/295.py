#优先队列
from heapq import *

class MedianFinder:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半，小大到小
        self.B = [] # 大顶堆，保存较小的一半，从小到大

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
        
#python里没有大顶堆，heapq是小顶堆，只能将小顶堆的push和pop改成'-'模拟大顶堆
#这个大顶堆只是名义上的大顶堆，实际上还是一个小顶堆，因为成员都是负的，但是执行逻辑和大顶堆一样，每一步只需要将符号删掉就是正常大顶堆的运行步骤

"""
小 524316 大
5           5<-
->2 5       2
4 5         4<- 2
->3 4 5     3 2
3 4 5       3<- 2 1
3-> 4 5 6   3 2 1

模拟
5           -5<-
->2 5       -2
4 5         -4< -2
->3 4 5     -3 -2
3 4 5       -3< -2 -1
->3 4 5 6   -3 -2 -1
"""


from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.nums = SortedList()
        self.left = self.right = None
        self.left_value = self.right_value = None

    def addNum(self, num: int) -> None:
        nums_ = self.nums

        n = len(nums_)
        nums_.add(num)

        if n == 0:
            self.left = self.right = 0
        else:
            # 模拟双指针，当 num 小于 self.left 或 self.right 指向的元素时，num 的加入会导致对应指针向右移动一个位置
            if num < self.left_value:
                self.left += 1
            if num < self.right_value:
                self.right += 1

            if n & 1:
                if num < self.left_value:
                    self.left -= 1
                else:
                    self.right += 1
            else:
                if self.left_value < num < self.right_value:
                    self.left += 1
                    self.right -= 1
                elif num >= self.right_value:
                    self.left += 1
                else:
                    self.right -= 1
                    self.left = self.right
        
        self.left_value = nums_[self.left]
        self.right_value = nums_[self.right]

    def findMedian(self) -> float:
        return (self.left_value + self.right_value) / 2
