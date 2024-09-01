class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target: return [-1,-1]
        # 搜索左边界 left
        i = 0
        
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        print(left,right)
        if left==right:
            return right-left-1
        elif left>right or (left<=0 and right<=0):
            return [-1,-1]
        else:
            return [left+1,right-1]
