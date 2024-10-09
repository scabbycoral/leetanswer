class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        j=len(nums)-1
        while i<=j:
            k=(i+j)//2
            #ij之间的位置公式
            #更好的是l+(r-l)//2
            if nums[k]==target:
                return k
            elif nums[k]>target:
                j=k-1
            else:
                i=k+1
        return -1
        
#递归
    def _binary_search(self, nums, target, left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self._binary_search(nums, target, left, mid - 1)
        else:
            return self._binary_search(nums, target, mid + 1, right)
