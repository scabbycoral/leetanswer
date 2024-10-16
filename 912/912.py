#插入排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for j in range(1,len(nums)):
            key=nums[j]
            i=j-1
            while i>=0 and nums[i]>key:
            #对于数组，这个while要倒着操作，变倒退边把无关元素后移
                nums[i+1]=nums[i]
                i-=1
            nums[i+1]=key
        return nums
#j从第二个开始，i从0到j。约定j是key
#时间复杂度o(n2)，空间复杂度o(1)
#在短数组（每个元素距离最终位置并不远），小区间上表现比较好
#在key之前的部分里找到key应该插入的地方并插入
"""最佳情况：T(n) = O(n)
最坏情况：T(n) = O(n2)
平均情况：T(n) = O(n2)"""

#归并排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        if len(nums) <= 1:  # 终止条件
            return nums
            
        mid = len(nums) // 2  # 找到中间索引
        left = self.sortArray(nums[:mid])  # 递归排序左半部分
        right = self.sortArray(nums[mid:])  # 递归排序右半部分
            
        return merge(left, right)  # 合并两个有序数组
#一直拆分到只有一个元素

#归并排序模板
#o(nlogn)，o(n)
class Solution:
    def merge(self, left, right):
        merged = []
        i, j = 0, 0
        # 合并两个已排序的列表
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                #count += len(left) - i
                merged.append(right[j])
                j += 1
        # 添加剩余元素
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def sortArray(self, nums: List[int]) -> List[int]:
        # 基本情况：如果列表为空或只有一个元素，则已排序
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2  # 找到中间索引
        # 递归排序左半部分和右半部分
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # 合并已排序的两部分
        return self.merge(left, right)
"""最佳情况：T(n) = O(n)
最差情况：T(n) = O(nlogn)
平均情况：T(n) = O(nlogn)"""
        
        
#选择排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            mini=i
            for j in range(i,len(nums)):
                if nums[j]<nums[mini]:
                    mini=j
            nums[i],nums[mini]=nums[mini],nums[i]
        return nums
#每次找到数组中最小的元素交换到未排序的第一个，数组分为前排序部分和后未排序部分
#o(n2)，o(1)
#贪心策略，之选当前最优。交换次数少，在交换成本高的任务中比较适合
"""最佳情况：T(n) = O(n2)
最差情况：T(n) = O(n2)
平均情况：T(n) = O(n2)"""

#快速排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, low, high):
            pivot_idx = random.randint(low, high)                   # 随机选择pivot
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]     # pivot放置到最左边
            pivot = arr[low]                                        # 选取最左边为pivot
            #不随机就可以直接选最左或者最右元素，随机就选择之后放到最左最右
            left, right = low, high     # 双指针
            while left < right:
                while left<right and arr[right] >= pivot:          # 找到右边第一个<pivot的元素
                    right -= 1
                arr[left] = arr[right]                             # 并将其移动到left处
                while left<right and arr[left] <= pivot:           # 找到左边第一个>pivot的元素
                    left += 1
                arr[right] = arr[left]                             # 并将其移动到right处
            arr[left] = pivot           # pivot放置到中间left=right处
            return left
        def quickSort(arr, low, high):
            if low < high:
                mid = partition(arr, low, high)     # 以mid为分割点
                quickSort(arr, low, mid-1)          # 递归对mid两侧元素进行排序
                quickSort(arr, mid+1, high)
        quickSort(nums, 0, len(nums)-1)         # 调用快排函数对nums进行排序
        return nums
#o(nlogn)，o(logn)
#单指针法：for i容易造成递归树倾斜
#找到比key小的移到左边，然后把key放到小于部分最后一个
for (int i = left + 1; i <= right; i++) {
    if (nums[i] < pivot) {
        lt++;
        swap(nums, i, lt);
    }
}
swap(nums, left, lt);
#双指针法：right、left避免倾斜
#左右同时进行，key放在已排序最后一个
#三指针法：将等于key的部分单独用i控制
#lr是左右边界，lt和gt是小于部分和大于部分的右左边界
int lt = left;
int gt = right + 1;
int i = left + 1;
while (i < gt) {
    if (nums[i] < pivot) {
        lt++;
        swap(nums, i, lt);
        i++;
    } else if (nums[i] == pivot) {
        i++;
    } else {
        gt--;
        swap(nums, i, gt);
    }
}
swap(nums, left, lt);
"""最佳情况：T(n) = O(nlogn)
最差情况：T(n) = O(n2)
平均情况：T(n) = O(nlogn)"""


#堆排序
class Solution:
    def sortArray(self, nums):
        n = len(nums)
        if n < 1:
            return nums

        # 1. 构建最大堆
        for i in range(n // 2 - 1, -1, -1):
            self.adjustHeap(nums, i, n)
            #从最后一个非叶子节点，从右向左，从下向上

        # 2. 循环将堆首位（最大值）与末位交换，然后重新调整最大堆
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.adjustHeap(nums, 0, i)  # 传入新的堆大小
            #大根堆每次转移首元素至末尾，最终结果就是升序排列

        return nums

    def adjustHeap(self, array, i, n):
        #i是待检测位置，n是未排序部分的大小
        maxIndex = i
        left = 2 * i + 1  # 左子树索引
        right = 2 * i + 2  # 右子树索引

        # 如果有左子树，且左子树大于父节点，则将最大指针指向左子树
        if left < n and array[left] > array[maxIndex]:
            maxIndex = left

        # 如果有右子树，且右子树大于当前最大值，则将最大指针指向右子树
        if right < n and array[right] > array[maxIndex]:
            maxIndex = right

        # 如果父节点不是最大值，则将父节点与最大值交换，并且递归调整与父节点交换的位置。
        if maxIndex != i:
            array[i], array[maxIndex] = array[maxIndex],array[i]
            self.adjustHeap(array, maxIndex, n)  # 递归调整
"""最佳情况：T(n) = O(nlogn)
最差情况：T(n) = O(nlogn)
平均情况：T(n) = O(nlogn)"""

#希尔排序
#不适合链表，因为总有从后往前找的逻辑，需要直接找到
class Solution:
    def sortArray(self, nums):
        length = len(nums)
        gap = length // 2  # 初始化间隔

        while gap > 0:
            print(gap)
            for i in range(gap, length):
                temp = nums[i]
                pre_index = i - gap
                #temp是当前元素，pre是对应的上一组元素

                #插入排序
                while pre_index >= 0 and nums[pre_index] > temp:
                    nums[pre_index + gap] = nums[pre_index]  # 移动元素
                    pre_index -= gap
                    

                nums[pre_index + gap] = temp  # 将 temp 插入合适位置

            gap //= 2  # 更新间隔

        return nums  # 返回排序后的数组
#通过gap大小对数组进行分组，对分组进行排序（也会影响到原数组）
#gap5的时候2个2个比，gap2的时候5个5个比，减少了比较和交换位置的次数
[8,9,1,7,2,3,5,4,6,0]
5
[3, 9, 1, 7, 2, 8, 5, 4, 6, 0]
[3, 5, 1, 7, 2, 8, 9, 4, 6, 0]
[3, 5, 1, 7, 2, 8, 9, 4, 6, 0]
[3, 5, 1, 6, 2, 8, 9, 4, 7, 0]
[3, 5, 1, 6, 0, 8, 9, 4, 7, 2]
2
[1, 5, 3, 6, 0, 8, 9, 4, 7, 2]
[1, 5, 3, 6, 0, 8, 9, 4, 7, 2]
[0, 5, 1, 6, 3, 8, 9, 4, 7, 2]
[0, 5, 1, 6, 3, 8, 9, 4, 7, 2]
[0, 5, 1, 6, 3, 8, 9, 4, 7, 2]
[0, 4, 1, 5, 3, 6, 9, 8, 7, 2]
[0, 4, 1, 5, 3, 6, 7, 8, 9, 2]
[0, 2, 1, 4, 3, 5, 7, 6, 9, 8]
1
[0, 2, 1, 4, 3, 5, 7, 6, 9, 8]
[0, 1, 2, 4, 3, 5, 7, 6, 9, 8]
[0, 1, 2, 4, 3, 5, 7, 6, 9, 8]
[0, 1, 2, 3, 4, 5, 7, 6, 9, 8]
[0, 1, 2, 3, 4, 5, 7, 6, 9, 8]
[0, 1, 2, 3, 4, 5, 7, 6, 9, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""最佳情况：T(n) = O(nlog2 n)
最坏情况：T(n) = O(nlog2 n)
平均情况：T(n) =O(nlog2n)"""


#冒泡排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 进行多次循环
        for i in range(n):
            #遍历所有元素
            for j in range(1, n - i):
                #从i开始，两两相邻元素进行比较排序
                #n-i是因为后面的i个元素是每一轮能找到的最大小元素，是已排序部分
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums
"""最佳情况：T(n) = O(n)
最差情况：T(n) = O(n2)
平均情况：T(n) = O(n2)"""


#计数排序

class Solution:

    def sortArray(self, nums):
        mini,maxi=min(nums),max(nums)
        count = [0] * (maxi-mini+1)
        
        #统计出现次数
        #为了减少冗余元素，将最小元素看作第1个
        for num in nums:
            count[num - mini] += 1
            
        #将统计次数更换为某字符出现的第一个位置，下一个字符出现的位置之前全是前一个相同的字符
        for i in range(1, (maxi-mini)+1):
            count[i] += count[i - 1]
        temp = nums.copy()
        #print(count)

        for i in range(len(nums) - 1, -1, -1):
            index = count[temp[i] - mini] - 1
            nums[index] = temp[i]
            count[temp[i] - mini] -= 1
            
        return nums
"""
当输入的元素是n 个0到k之间的整数时，它的运行时间是 O(n + k)。计数排序不是比较排序，排序
的速度快于任何比较排序算法。由于用来计数的数组C的长度取决于待排序数组中数据的范围
（等于待排序数组的最大值与最小值的差加上1），这使得
计数排序对于数据范围很大的数组，需要大量时间和内存。

最佳情况：T(n) = O(n+k)
最差情况：T(n) = O(n+k)
平均情况：T(n) = O(n+k)
"""

#基数排序
class Solution:
    def sortArray(self, nums):
        if not nums:
            return nums

        # 找到最小值和最大值
        min_val = min(nums)
        max_val = max(nums)

        # 计算值的范围
        range_size = max_val - min_val + 1
        nums = [num - min_val for num in nums]  # 使所有数 >= 0
        print(nums)
        # 计算最大位数
        max_len = self.getMaxLen(max_val - min_val)

        count = [0] * 10
        temp = [0] * len(nums)

        divisor = 1
        #表示当前处理位数
        print(nums)
        for _ in range(max_len):
            self.countingSort(nums, temp, divisor, count)
            nums, temp = temp, nums  # 交换引用
            divisor *= 10
            print(nums)

        return [num + min_val for num in nums]  # 恢复原始值

    def countingSort(self, nums, res, divisor, count):
        # 1. 计算计数数组，计算第divisor位
        for num in nums:
            remainder = (num // divisor) % 10
            count[remainder] += 1
        # 2. 变成位置数组
        for i in range(1, 10):
            count[i] += count[i - 1]

        # 3. 从后向前赋值
        for i in range(len(nums) - 1, -1, -1):
            remainder = (nums[i] // divisor) % 10
            index = count[remainder] - 1
            res[index] = nums[i]
            count[remainder] -= 1

        # 4. 重置计数数组
        count[:] = [0] * 10

    def getMaxLen(self, num):
        max_len = 0
        while num > 0:
            num //= 10
            max_len += 1
        return max_len
"""
最佳情况：T(n) = O(n * k)
最差情况：T(n) = O(n * k)
平均情况：T(n) = O(n * k)

MSD 从高位开始进行排序
LSD 从低位开始进行排序
"""

#桶排序
#避免使用递归，由于桶个数，max函数会导致递归层数超过1000
class Solution:
    def sortArray(self, nums):
        array = nums
        bucket_size = 10
        
        if array is None or len(array) < 2:
            return array

        # 找到最大值和最小值
        max_val = max(array)
        min_val = min(array)

        # 计算桶的数量
        bucket_count = (max_val - min_val) // bucket_size + 1
        bucket_arr = [[] for _ in range(bucket_count)]
        result_arr = []

        # 将元素分配到桶中
        for num in array:
            bucket_index = (num - min_val) // bucket_size
            bucket_arr[bucket_index].append(num)

        # 对每个桶进行插入排序并合并
        for bucket in bucket_arr:
            if bucket:  # 检查桶是否非空
                self.insertionSort(bucket)
                result_arr.extend(bucket)

        return result_arr

    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > temp:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp
"""
桶排序最好情况下使用线性时间O(n)，桶排序的时间复杂度，取决与对各个桶之间数据进行排序的时间复杂度，因为其它部分的时间复杂度都为O(n)。很显然，桶划分的越小，各个桶之间的数据越少，排序所用的时间也会越少。但相应的空间消耗就会增大。
最佳情况：T(n) = O(n+k)
最差情况：T(n) = O(n+k)
平均情况：T(n) = O(n2)
"""