#以下方法都是k之前进行增大窗口，k之后一个一个判断

#优先级队列模拟大根堆
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        #将一个list变成大根堆，先取反
        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            print(q)
            while q[0][1] <= i - k:
                heapq.heappop(q)
                #最大值如果在窗口外就出去，小值不用管
            ans.append(-q[0][0])
        return ans

#双端队列模拟大根堆，不需要当作负数进行
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        #双端队列保存一个大根堆
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
                #不保存比末尾更小的元素，如果更大就挤出去一个
            q.append(i)
            print(q)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        # 未形成窗口
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        # 形成窗口后
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res

#用max判断十分缓慢，建议用双端队列