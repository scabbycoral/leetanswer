class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    #摩尔投票法
    #专门拿来寻找众数
        votes = 0
        for num in nums:
            if votes == 0: x = num
            #更新当前值
            #只有vote为0才更新众数值
            votes += 1 if num == x else -1
            #和众数是否一样
            
        """
        # 验证 x 是否为众数
        for num in nums:
            if num == x: count += 1
        return x if count > len(nums) // 2 else 0 # 当无众数时返回 0
        """
        return x
