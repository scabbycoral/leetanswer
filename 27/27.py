# Python file for number 27 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return left
        
#只统计不用删除的 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for j in nums:
            if j!=val:
                nums[i]=j
                i+=1
                