class Solution:
    def merge(self,left, right, res):
        merged = []
        i, j = 0, 0
        # 合并两个已排序的列表并计数
        while i < len(left) and j < len(right):
            if left[i][0] > right[j][0]:  # 注意这里比较的是值而不是索引
                
                res[left[i][1]] += len(right) - j  # 计数右侧小于当前元素的个数
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # 添加剩余元素
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def sortAndCount(self, indices, res) -> List[Tuple[int, int]]:
        if len(indices) <= 1:
            return indices
        
        mid = len(indices) // 2  # 找到中间索引
        # 递归排序左半部分和右半部分
        left = self.sortAndCount(indices[:mid], res)
        right = self.sortAndCount(indices[mid:], res)
        
        # 合并已排序的两部分
        return self.merge(left, right, res)

    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        indices = [(nums[i], i) for i in range(len(nums))]
        self.sortAndCount(indices, res)
        return res
#因为本题考虑到顺序，所以需要indices记录最初位置
#LCR170不考虑顺序，所以直接用nums即可


#离散化树状数组
class FenwickTree:
    def __init__(self, length):
        self.c = [0] * (length + 1)  # 树状数组

    def low_bit(self, x):
        return x & (-x)

    def update(self, pos):
        while pos < len(self.c):
            self.c[pos] += 1
            pos += self.low_bit(pos)

    def query(self, pos):
        ret = 0
        while pos > 0:
            ret += self.c[pos]
            pos -= self.low_bit(pos)
        return ret

class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []

        # 离散化
        a = sorted(set(nums))  # 去重并排序
        n = len(a)
        fenwick_tree = FenwickTree(n)

        result = []
        for num in reversed(nums):
            # 获取离散化后的索引
            idx = bisect.bisect_left(a, num) + 1
            result.append(fenwick_tree.query(idx - 1))  # 查询小于当前元素的个数
            fenwick_tree.update(idx)  # 更新当前元素的计数

        return result[::-1]  # 反转结果以恢复正确顺序
