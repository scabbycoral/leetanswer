# Python file for number 26 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        for j in range(1,len(nums)):
            if nums[j]!=nums[j-1]:
                nums[i]=nums[j]
                i+=1
        return i
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow
