#插入排序
#因为本题的第一个节点就有可能被移动，所以返回head没有意义，head有可能已经成为别的节点，需要一个虚拟节点在函数一开始就指向head
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode(-1)
        #res.next=head
        #不能连上，因为不知道head会指向那里
        key=head
        while key:
            tmp=key.next
            #1.1记录key取出位置
            pre=res
            while pre.next and pre.next.val<key.val:
                pre=pre.next
            key.next=pre.next
            pre.next=key
            #2.合适位置插入，pre.next
            #res初始时后面是没有节点的，通过pre.next不断连接转移的节点
            key=tmp
            #1.2将取出key位置的空缺连上
        return res.next
#时间复杂度o(n2)，空间复杂度o(1)

#归并排序递归，自上而下
#通过快慢指针找中点
#时间复杂度o(nlogn)，空间复杂度o(n)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(first_half, second_half):
            dummy = ListNode()
            tail = dummy

            # Merge two sorted linked lists
            while first_half and second_half:
                if first_half.val < second_half.val:
                    tail.next = first_half
                    first_half = first_half.next
                else:
                    tail.next = second_half
                    second_half = second_half.next
                tail = tail.next

            # Attach the remaining nodes
            if first_half:
                tail.next = first_half
            elif second_half:
                tail.next = second_half

            return dummy.next

        # Base case: if the list is empty or has one element
        if not head or not head.next:
            return head

        # Split the list into two halves
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first_half = head
        second_half = slow.next
        slow.next = None  # Split the list into two halves

        # Recursively sort the two halves
        first_half = self.sortList(first_half)
        second_half = self.sortList(second_half)

        # Merge the sorted halves
        return merge(first_half, second_half)

#归并排序迭代，自下而上
#时间复杂度o(nlogn)，空间复杂度o(1)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        #intv是单元长度，把链表分割为intv长度的n个部分
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        while intv < length:
            pre, h = res, res.next
            while h:
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                #取i个元素为链表
                if i: break
                #如果i不是0说明h1中没有元素
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h 
            intv *= 2
        return res.next

#归并排序模板
#o(nlogn)，o(n)
class Solution:
    def merge(self, left, right):
        # 创建一个虚拟头节点以便于合并
        dummy = ListNode(0)
        current = dummy

        # 合并两个已排序的链表
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # 添加剩余元素
        if left:
            current.next = left
        elif right:
            current.next = right
        
        return dummy.next  # 返回合并后的链表头节点

    def sortList(self, head: ListNode) -> ListNode:
        # 基本情况：如果链表为空或只有一个节点，则已排序
        if not head or not head.next:
            return head
        
        # 找到中间节点并拆分链表
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left_head=head
        right_head = slow.next
        slow.next = None  # 拆分链表
        
        # 递归排序左右两部分
        left_sorted = self.sortList(left_head)
        right_sorted = self.sortList(right_head)
        
        # 合并已排序的两部分
        return self.merge(left_sorted, right_sorted)


#选择排序
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        sorted_head = ListNode(0)  # 创建一个新的头节点
        last_sorted = sorted_head  # 指向已排序部分的尾部

        while head:
            # 找到最小节点
            min_cur = head
            min_pre = None
            prev = head
            #prev指向后未排序部分
            while prev.next:
                if prev.next.val < min_cur.val:
                    min_cur = prev.next
                    min_pre = prev
                prev = prev.next
            
            # 从原链表中删除最小节点
            if min_pre:
                min_pre.next = min_cur.next
            else:
                head = head.next  # 如果最小节点是头节点，更新头节点
            
            # 将最小节点添加到已排序链表
            last_sorted.next = min_cur
            last_sorted = min_cur
            last_sorted.next = None  # 断开最小节点的next指针

        return sorted_head.next  # 返回已排序链表的头节点
#贪心策略，之选当前最优。交换次数少，在交换成本高的任务中比较适合
#每次找到数组中最小的元素交换到未排序的第一个，数组分为前排序部分和后未排序部分
#o(n2)，o(1)

#快速排序，迭代
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        sorted_head = ListNode(0)  # 创建一个新的头节点
        last_sorted = sorted_head  # 指向已排序部分的尾部

        while head:
            # 找到最小节点
            min_cur = head
            min_pre = None
            prev = head
            #prev指向后未排序部分
            while prev.next:
                if prev.next.val < min_cur.val:
                    min_cur = prev.next
                    min_pre = prev
                prev = prev.next
            
            # 从原链表中删除最小节点
            if min_pre:
                min_pre.next = min_cur.next
            else:
                head = head.next  # 如果最小节点是头节点，更新头节点
            
            # 将最小节点添加到已排序链表
            last_sorted.next = min_cur
            last_sorted = min_cur
            last_sorted.next = None  # 断开最小节点的next指针

        return sorted_head.next  # 返回已排序链表的头节点
#快速排序，递归
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # 空链表或只有一个节点直接返回
        
        # 分割链表
        def partition(head, pivot):
            before_head = ListNode(0)  # 小于区的虚拟头节点
            after_head = ListNode(0)   # 大于区的虚拟头节点
            before = before_head
            after = after_head
            
            while head:
                if head.val < pivot:
                    before.next = head
                    before = before.next
                else:
                    after.next = head
                    after = after.next
                head = head.next
            
            before.next = None  # 结束小于区
            after.next = None   # 结束大于区
            return before_head.next, after_head.next  # 返回两个链表的头节点
        
        # 选择一个随机的pivot
        def getRandomNode(head):
            count = 0
            node = head
            while node:
                count += 1
                node = node.next
            
            random_index = random.randint(0, count - 1)
            node = head
            for _ in range(random_index):
                node = node.next
            return node
        
        pivot = getRandomNode(head).val  # 随机选择一个pivot
        less_head, greater_head = partition(head, pivot)  # 分割链表

        # 递归排序两个子链表
        sorted_less = self.sortList(less_head)
        sorted_greater = self.sortList(greater_head)

        # 合并排序后的链表
        if not sorted_less:
            return sorted_greater
        
        # 找到sorted_less的尾部
        tail = sorted_less
        while tail.next:
            tail = tail.next
        
        tail.next = sorted_greater  # 连接两个链表
        return sorted_less
        
#堆排序

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 将链表转换为数组
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next

        # 使用堆排序对数组进行排序
        self.heapSort(nums)

        # 将排序后的数组转换回链表
        sorted_head = ListNode(0)  # 虚拟头节点
        current = sorted_head
        for num in nums:
            current.next = ListNode(num)
            current = current.next

        return sorted_head.next

    def heapSort(self, nums):
        n = len(nums)
        if n <= 1:
            return

        # 构建最大堆
        for i in range(n // 2 - 1, -1, -1):
            self.adjustHeap(nums, i, n)

        # 循环将堆首位（最大值）与末位交换，然后重新调整最大堆
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.adjustHeap(nums, 0, i)

    def adjustHeap(self, array, i, n):
        maxIndex = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[left] > array[maxIndex]:
            maxIndex = left
        if right < n and array[right] > array[maxIndex]:
            maxIndex = right

        if maxIndex != i:
            array[i], array[maxIndex] = array[maxIndex], array[i]
            self.adjustHeap(array, maxIndex, n)
#o(nlogn)，递归o(n)，迭代o(1)