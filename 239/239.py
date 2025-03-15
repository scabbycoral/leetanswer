#以下方法都是k之前进行增大窗口，k之后一个一个判断

#优先级队列模拟大根堆
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        #创建一个枚举，并把每个元素取反，用来组成大根堆
        heapq.heapify(q)
        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
            #因为有可能保存了n个已经在范围外的最大值，因为堆不考虑堆顶以外的检查
                heapq.heappop(q)
                #q[0][1]是最大值原本的位置
                #最大值如果在窗口外就出去，小值不用管
            ans.append(-q[0][0])
        return ans




#用max判断十分缓慢，建议用双端队列