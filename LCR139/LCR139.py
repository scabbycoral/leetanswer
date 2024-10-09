#首尾指针
class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        i=0
        j=len(actions)-1
        while i<j:
            while i<j and actions[i]&1==1:
                i+=1
            while i<j and actions[j]&1==0:
                j-=1
            actions[i],actions[j]=actions[j],actions[i]
        return actions
        
#快慢指针
class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        low, fast = 0, 0
        while fast < len(actions):
            if actions[fast] & 1:  # 检查是否为奇数
                actions[low], actions[fast] = actions[fast], actions[low]  # 交换奇数到前面
                low += 1  # 更新奇数放置位置
            fast += 1  # 移动到下一个元素
        return actions
#本题是数组重排序

#双端队列
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        tmp = collections.deque()
        for num in nums:
            tmp.appendleft(num) if num % 2 ==1 else tmp.append(num)
        return list(tmp)
        #或者创建一个list，用insert代替appendleft