class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 0  # 起点
        r = 0  # 终点
        maxLen = 0  # 待返回的最长长度

        while r < len(nums):
            if r == l or nums[r - 1] < nums[r]:  # 保持递增
            ##r==l包含l=0,r=0的情况
                maxLen = max(maxLen, r - l + 1)  # 比较取大
                r += 1  # 终点前进
            else:  # 递增中断
                l = r  # 更新起点

        return maxLen
