#归并排序
#record的顺序是确定的，要得到的时候前一个比后一个大的一对数据
#实际上对归并排序增加一个检测逆序对的if或者右侧大于左侧之后的一个计数+1即可

#下面是方便理解的方法，有很多地方冗余
class Solution:
    def __init__(self):
        self.count = 0

    def reversePairs(self, nums):
        self.count = 0
        self.merge_sort(nums, 0, len(nums) - 1)
        return self.count

    def merge_sort(self, nums, left, right):
        if left < right:
            mid = left + (right - left) // 2
            self.merge_sort(nums, left, mid)
            self.merge_sort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        temparr = []
        temp1, temp2 = left, mid + 1

        # Count reverse pairs and merge the two halves
        while temp1 <= mid and temp2 <= right:
            if nums[temp1] <= nums[temp2]:
                temparr.append(nums[temp1])
                temp1 += 1
            else:
                # Count how many elements in the left half are greater than nums[temp2]
                self.count += (mid - temp1 + 1)
                temparr.append(nums[temp2])
                temp2 += 1
        #合并的同时统计逆序对，temp1指向前半部分，temp2指向后半部分
        #合并之后指针分离到两个部分，不会计算到重复逆序对

        # Copy remaining elements from the left half
        while temp1 <= mid:
            temparr.append(nums[temp1])
            temp1 += 1

        # Copy remaining elements from the right half
        while temp2 <= right:
            temparr.append(nums[temp2])
            temp2 += 1

        # Copy the merged elements back into the original array
        for i in range(len(temparr)):
            nums[left + i] = temparr[i]
            
#符合归并排序的模板
class Solution:
    def reversePairs(self, record: List[int]) -> int:
        def merge(left: List[int], right: List[int]) -> (List[int], int):
            merged = []
            i, j = 0, 0
            count = 0
            
            # 合并两个已排序的列表并统计逆序对
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    # 逆序对的数量等于左半部分剩余的元素数量
                    print(left,right,left[i],right[j])
                    count += len(left) - i
                    merged.append(right[j])
                    j += 1
            
            # 添加剩余元素
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged, count

        def sort_and_count(nums: List[int]) -> (List[int], int):
            # 基本情况：如果列表为空或只有一个元素，则已排序
            if len(nums) <= 1:
                return nums, 0
            
            mid = len(nums) // 2  # 找到中间索引
            # 递归排序左半部分和右半部分
            left, left_count = sort_and_count(nums[:mid])
            right, right_count = sort_and_count(nums[mid:])
            
            # 合并已排序的两部分并统计逆序对
            merged, merge_count = merge(left, right)
            
            # 总逆序对数量是左右部分的逆序对数量加上合并过程中统计的逆序对数量
            return merged, left_count + right_count + merge_count

        # 调用排序和计数函数
        _, total_reverse_pairs = sort_and_count(record)
        return total_reverse_pairs
#因为本题不考虑顺序，所以直接用nums即可
#315考虑顺序，所以需要indices记录最初位置
            
            
#离散化树状数组
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & (-x)
    
    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.tree[x]
            x -= BIT.lowbit(x)
        return ret

    def update(self, x):
        while x <= self.n:
            self.tree[x] += 1
            x += BIT.lowbit(x)

class Solution:
    def reversePairs(self, record: List[int]) -> int:
        n = len(record)
        # 离散化
        tmp = sorted(record)
        for i in range(n):
            record[i] = bisect.bisect_left(tmp, record[i]) + 1
        # 树状数组统计逆序对
        bit = BIT(n)
        ans = 0
        for i in range(n - 1, -1, -1):
            ans += bit.query(record[i] - 1)
            bit.update(record[i])
        return ans
