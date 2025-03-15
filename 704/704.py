#线性查找，最好最坏情况o(n)
class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

#二分查找
#最好最坏情况o(logn)
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

#跳跃查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        # 计算步长
        step = int(math.sqrt(n))

        # 跳跃过程
        prev = 0
        while nums[min(step, n) - 1] < target:
            prev = step
            step += step
            print(step)
            if prev >= n:
                return -1
            
        # 线性搜索
        for i in range(prev, min(step, n)):
            if nums[i] == target:
                return i

        # 如果未找到目标值，返回 -1
        return -1
        
#插值搜索
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r and nums[l]<=target<=nums[r]:
            mid=l+((target-nums[l])*(r-l)//(nums[r]-nums[l]))
            if nums[mid]==target:return mid
            elif nums[mid]>target:r=mid-1
            else:l=mid+1
        return -1
        
#指数搜索
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, left, right):
            if left > right:
                return -1
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(nums, target, left, mid - 1)
            else:
                return binary_search(nums, target, mid + 1, right)
        i = 1
        while i < len(nums) and nums[i] <= target:
            i *= 2
        return binary_search(nums, target, i // 2, min(i, len(nums) - 1))
        
#斐波那契搜索
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        fib_k_minus_2 = 0  # F_{k-2}
        fib_k_minus_1 = 1  # F_{k-1}
        fib_k = fib_k_minus_1 + fib_k_minus_2  # F_k

        while fib_k < n:
            fib_k_minus_2 = fib_k_minus_1
            fib_k_minus_1 = fib_k
            fib_k = fib_k_minus_1 + fib_k_minus_2
        #表示每个部分有fib个，所以后面要-1，找到使fib刚刚比n大的fib12组合
        # 初始化搜索范围
        offset = -1
        while fib_k > 1:
            # 计算划分点
            i = min(offset + fib_k_minus_2, n - 1)

            # 比较目标值与划分点的值
            if nums[i] < target:
                # 目标值在右半部分
                fib_k = fib_k_minus_1
                fib_k_minus_1 = fib_k_minus_2
                fib_k_minus_2 = fib_k - fib_k_minus_1
                offset = i
            elif nums[i] > target:
                # 目标值在左半部分
                fib_k = fib_k_minus_2
                fib_k_minus_1 = fib_k_minus_1 - fib_k_minus_2
                fib_k_minus_2 = fib_k - fib_k_minus_1
            else:
                # 找到目标值
                return i
            print(fib_k_minus_2,fib_k_minus_1,fib_k)

        # 检查最后一个元素
        #只剩下一个元素，一定是1
        if fib_k_minus_1 and nums[offset + 1] == target:
            return offset + 1

        # 如果未找到目标值，返回 -1
        return -1
#data[0,1,2,3,4,5,6,7,8,9]target[2]offset=-1
#data[0,1,2,3,4,5,6,7,8,9,9,9,9]fib=13,fib2=5,fib1=8
#data1[0,1,2,3,4]data2[5,6,7,8,9,9,9,9]i[4]
#∵4>2∴fib=5,fib2=2,fib1=3
#data1[0,1]data2[2,3,4]i[1]
#∵1<2∴offset=1,fib=3,fib2=1,fib1=2
#data1[2]data2[3,4]i[2]