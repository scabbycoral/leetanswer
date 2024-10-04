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
#本题是数组重排序


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        tmp = collections.deque()
        for num in nums:
            tmp.appendleft(num) if num % 2 ==1 else tmp.append(num)
        return list(tmp)