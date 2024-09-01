class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #相同数字异或为0
        x = 0
        for num in nums:  # 1. 遍历 nums 执行异或运算
            a=x
            x ^= num
            print(a,num,x)      
        return x;         # 2. 返回出现一次的数字 x
