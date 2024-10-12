class HashNode:
    """哈希表的节点类"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # 指向下一个节点

#散列函数，链接法
class HashTable:
    """哈希表类"""
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size  # 初始化哈希表
        self.count = 0  # 记录当前存储的元素数量

    def _hash(self, key):
        """哈希函数"""
        #hash(key)从key找value
        return hash(key) % self.size#除法散列法

    def insert(self, key, value):
        """插入键值对"""
        if self.count >= self.size * 0.7:  # 负载因子超过0.7时扩展
            self._resize()

        index = self._hash(key)
        new_node = HashNode(key, value)

        if not self.table[index]:
            self.table[index] = new_node
            #如果节点为空
        else:
            current = self.table[index]
            while True:
                if current.key == key:  # 如果键已经存在，更新值
                    current.value = value
                    return
                
                current = current.next
                #找到末尾
                if current.next is None:  # 不存在，末尾添加
                    current.next = new_node
                    return
                current = current.next

        self.count += 1

    def search(self, key):
        """查找键对应的值"""
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None  # 如果未找到，返回 None

    def delete(self, key):
        """删除键值对"""
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next  # 删除头节点
                self.count -= 1
                return True  # 删除成功
            prev = current
            current = current.next

        return False  # 如果未找到，返回 False

    def _resize(self):
        """扩容哈希表"""
        old_table = self.table
        self.size *= 2  # 扩大一倍
        self.table = [None] * self.size
        self.count = 0

        for head in old_table:
            current = head
            while current:
                self.insert(current.key, current.value)  # 重新插入元素
                current = current.next

    def __str__(self):
        """打印哈希表内容"""
        return str([(node.key, node.value) for node in self.table if node])


#开放寻址法，线性探查
class HashTable:
    """哈希表类"""
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size  # 初始化哈希表
        self.count = 0  # 记录当前存储的元素数量

    def _hash(self, key):
        """哈希函数"""
        return hash(key) % self.size  # 除法散列法

    def insert(self, key, value):
        """插入键值对"""
        if self.count >= self.size * 0.7:  # 如果负载因子超过0.7，可能需要扩容
            self._resize()

        index = self._hash(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:  # 如果键已经存在，更新值
                self.table[index] = (key, value)
                return
            i += 1
            index = (self._hash(key) + i) % self.size  # 使用线性探查公式

        self.table[index] = (key, value)  # 插入新键值对
        self.count += 1

    def search(self, key):
        """查找键对应的值"""
        index = self._hash(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
            index = (self._hash(key) + i) % self.size  # 使用线性探查公式

        return None  # 如果未找到，返回 None

    def delete(self, key):
        """删除键值对"""
        index = self._hash(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # 删除键值对
                self.count -= 1
                return True
            i += 1
            index = (self._hash(key) + i) % self.size  # 使用线性探查公式

        return False  # 如果未找到，返回 False

    def _resize(self):
        """扩容哈希表"""
        old_table = self.table
        self.size *= 2  # 扩大一倍
        self.table = [None] * self.size
        self.count = 0

        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])  # 重新插入元素

    def __str__(self):
        """打印哈希表内容"""
        return str([(k, v) for k, v in self.table if k is not None])
        
#二次探查
class HashTable:
    """哈希表类"""
    def __init__(self, size=10, c1=1, c2=1):
        self.size = size
        self.table = [None] * self.size  # 初始化哈希表
        self.count = 0  # 记录当前存储的元素数量
        self.c1 = c1  # 线性探查系数
        self.c2 = c2  # 二次探查系数

    def _hash(self, key):
        """哈希函数"""
        return hash(key) % self.size  # 除法散列法

    def insert(self, key, value):
        """插入键值对"""
        if self.count >= self.size * 0.7:  # 如果负载因子超过0.7，可能需要扩容
            self._resize()

        index = self._hash(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:  # 如果键已经存在，更新值
                self.table[index] = (key, value)
                return
            i += 1
            index = (self._hash(key) + self.c1 * i + self.c2 * i * i) % self.size  # 使用公式

        self.table[index] = (key, value)  # 插入新键值对
        self.count += 1

    def search(self, key):
        """查找键对应的值"""
        index = self._hash(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
            index = (self._hash(key) + self.c1 * i + self.c2 * i * i) % self.size  # 使用公式

        return None  # 如果未找到，返回 None

    def delete(self, key):
        """删除键值对"""
        index = self._hash(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # 删除键值对
                self.count -= 1
                return True
            i += 1
            index = (self._hash(key) + self.c1 * i + self.c2 * i * i) % self.size  # 使用公式

        return False  # 如果未找到，返回 False

    def _resize(self):
        """扩容哈希表"""
        old_table = self.table
        self.size *= 2  # 扩大一倍
        self.table = [None] * self.size
        self.count = 0

        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])  # 重新插入元素

    def __str__(self):
        """打印哈希表内容"""
        return str([(k, v) for k, v in self.table if k is not None])

"""
选择 \( c_1 \) 和 \( c_2 \) 的值通常依赖于具体应用和性能要求。以下是一些常见的选择原则和建议：

1. **默认值**：
   - 一般情况下，可以选择 \( c_1 = 1 \) 和 \( c_2 = 1 \)。这意味着探查过程中线性和二次部分同等重要。

2. **线性与二次探查的平衡**：
   - 如果发现哈希表的冲突较多，可以考虑增大 \( c_2 \) 的值，以增强二次探查的效果，帮助减少聚集现象。

3. **减少聚集**：
   - 选择 \( c_1 = 0 \) 和 \( c_2 = 1 \) 将会完全依赖于二次探查，可能有助于减少聚集，但也可能会增加查找时间。

4. **实验与调整**：
   - 根据具体数据和负载特征进行实验，观察性能表现。可以在实际使用中动态调整这些参数，找到最适合的数据分布和查询模式的组合。

5. **常用值**：
   - 在某些实现中，常见的选择包括 \( c_1 = 1 \) 和 \( c_2 = 0.5 \)，这能在一定程度上利用线性探查，同时减少冲突的影响。

### 实际例子

- **插入与查找性能**：如果在测试中发现插入操作慢而查找操作快，可能需要增加 \( c_2 \) 来更有效地解决冲突。
- **负载因子**：在负载因子较高的情况下，可以尝试降低 \( c_1 \) 的值来减少冲突。

### 结论
选择 \( c_1 \) 和 \( c_2 \) 的过程往往是实验性的，需要根据具体情况进行调整。通常从简单的默认值开始，然后逐步优化是一个好的实践。如果您有具体的应用场景，我可以给出更详细的建议！
"""

#双重散列
class HashTable:
    """哈希表类"""
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size  # 初始化哈希表
        self.count = 0  # 记录当前存储的元素数量

    def _hash1(self, key):
        """第一个哈希函数"""
        return hash(key) % self.size  # 除法散列法

    def _hash2(self, key):
        """第二个哈希函数"""
        return 1 + (hash(key) % (self.size - 1))  # 确保步长不为零

    def insert(self, key, value):
        """插入键值对"""
        if self.count >= self.size * 0.7:  # 如果负载因子超过0.7，可能需要扩容
            self._resize()

        index = self._hash1(key)
        step = self._hash2(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:  # 如果键已经存在，更新值
                self.table[index] = (key, value)
                return
            i += 1
            index = (self._hash1(key) + i * step) % self.size  # 使用双重散列公式

        self.table[index] = (key, value)  # 插入新键值对
        self.count += 1

    def search(self, key):
        """查找键对应的值"""
        index = self._hash1(key)
        step = self._hash2(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
            index = (self._hash1(key) + i * step) % self.size  # 使用双重散列公式

        return None  # 如果未找到，返回 None

    def delete(self, key):
        """删除键值对"""
        index = self._hash1(key)
        step = self._hash2(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # 删除键值对
                self.count -= 1
                return True
            i += 1
            index = (self._hash1(key) + i * step) % self.size  # 使用双重散列公式

        return False  # 如果未找到，返回 False

    def _resize(self):
        """扩容哈希表"""
        old_table = self.table
        self.size *= 2  # 扩大一倍
        self.table = [None] * self.size
        self.count = 0

        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])  # 重新插入元素

    def __str__(self):
        """打印哈希表内容"""
        return str([(k, v) for k, v in self.table if k is not None])

#完全散列，针对静态数据，插入不会让散列表以前的数据发生变化
class PerfectHashTable:
    """完全散列哈希表类"""

    def __init__(self, keys, size):
        self.size = size  # 外层散列表的大小
        self.table = [None] * self.size  # 外层散列表
        self.sub_tables = [None] * self.size  # 子哈希表
        self.p = self._find_next_prime(size)  # 选择一个大于 size 的质数
        self._build(keys)

    def _find_next_prime(self, n):
        """查找下一个质数"""
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        while not is_prime(n):
            n += 1
        return n

    def _outer_hash(self, key):
        """外层散列函数"""
        return key % self.size  # 简单的取模散列

    def _inner_hash(self, key, a, b, sub_table_size):
        """内层散列函数"""
        return ((a * key + b) % self.p) % sub_table_size

    def _build(self, keys):
        """构建完全散列哈希表"""
        #自动调整内层长度
        for key in keys:
            index = self._outer_hash(key)
            if self.table[index] is None:
                # 初始化子哈希表为一个空列表
                self.sub_tables[index] = []
                self.table[index] = key  # 存储外层键

            # 获取内层表的散列函数参数
            a = len(self.sub_tables[index]) + 1  # 使用当前元素数量作为 a
            b = len(self.sub_tables[index]) + 1  # 使用当前元素数量作为 b

            # 计算内层哈希值
            inner_index = self._inner_hash(key, a, b, len(self.sub_tables[index]) + 1)

            # 将键插入子哈希表
            # 确保内层表足够长
            while len(self.sub_tables[index]) <= inner_index:
                self.sub_tables[index].append(None)

            self.sub_tables[index][inner_index] = key  # 存储键

    def search(self, key):
        """查找键是否存在"""
        index = self._outer_hash(key)
        if self.table[index] is None:
            return False
        
        # 获取内层表的参数
        a = len(self.sub_tables[index]) + 1  # 使用当前元素数量作为 a
        b = len(self.sub_tables[index]) + 1  # 使用当前元素数量作为 b
        inner_index = self._inner_hash(key, a, b, len(self.sub_tables[index]) + 1)

        # 检查键是否存在
        return self.sub_tables[index][inner_index] == key  

    def display(self):
        """打印完整的散列表内容"""
        for i in range(self.size):
            if self.table[i] is not None:
                print(f"外层索引 {i}: 键 = {self.table[i]}, 内层散列内容 = {self.sub_tables[i]}")
            else:
                print(f"外层索引 {i}: 空")

# 示例调用
if __name__ == "__main__":
    keys = [10, 22, 37, 40, 52, 60, 70, 72, 75]
    size = 10  # 外层散列表的大小
    hash_table = PerfectHashTable(keys, size)

    for i in range(9):
        if hash_table.table[i] is not None:
            print(f"外层索引 {i}: 键 = {hash_table.table[i]}, 内层散列内容 = {hash_table.sub_tables[i]}")
        else:
            print(f"外层索引 {i}: 空")
#内层散列和外层散列方法不一样，外层size为入参长度，内层size为散列进入的元素个数平方（由于python用的是dict所以不需要设定长度）
#每个内层散列函数参数都不一样