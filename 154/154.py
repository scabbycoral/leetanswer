class Solution:
    def findMin(self, nums: [int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] > nums[j]: i = m + 1
            elif nums[m] < nums[j]: j = m
            else: j -= 1
        return nums[i]
#如果nums[m]比j大，说明m属于前半部分，则舍去前半部分中比m大的部分
#如果比j小则说明，m属于后半部分，要舍去后半部分中比m大的
#如果相等，无法判断在前半还是后半，[3,3,1,3]，[3,1,3,3]，不管是不是最小值，都去掉一个，不影响结果

#两种方法，剑指offer是前后一起比，这个是只和最后一个比