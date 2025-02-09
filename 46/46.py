class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))   # 添加排列方案
                return
            for i in range(x, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]
                #从0开始，从前往后，用x和后面的元素依次交换
                #x依次递增，x递增时，x前面的元素固定
        res = []
        dfs(0)
        return res
