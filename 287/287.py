class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        """
        #方法一，哈希表
        #不用列表是因为哈希表查找和插入的时间复杂度是O(1)，列表是O(n)
        hmap=set()
        for i in documents:
            if i in hmap:
                return i
            hmap.add(i)
        return
        """
        
        """
        #方法二，静态表原地交换
        #从头到尾遍历，遍历条件是数值等于位置，否则进行交换，交换时如果两个位置值一样则返回
        i=0
        while i<len(documents):
            if documents[i]==i:
                i+=1
                continue
                #位置正确且没冲突，继续找下一个
            elif documents[i]==documents[documents[i]]:
                return documents[i]
                #位置不正确且要交换的位置保存了同样的值
            else:
                documents[documents[i]],documents[i]=documents[i],documents[documents[i]]
                #位置不正确且不冲突则交换位置
        return -1
        """
        
        """
        #二分法
        #不是将原数组进行二分，而是对里面可能存在的元素进行二分，看哪些元素有重复，每进行一次二分，都用这些元素对整个nums进行判断
        def countRange(nums, length, start, end) -> int:
            count = 0
            for i in range(length):
                if nums[i] >= start and nums[i] <= end:
                    count+=1
                i+=1
            return count

        length=len(nums)

        start = 1
        end = length - 1
        #start和end表示的不是位置，是从1到n的数字，也可以理解为1-n数字的下标
        while end >= start:
            middle = ((end - start) >> 1) + start
            #当前后指针都是动态时，计算中间位置，这里代表中间位置的数字，因为num大小是从1到n
            count = countRange(nums, length, start, middle)
            if end == start:
                if count > 1:
                    return start
                else:
                    break

            if count > (middle - start + 1):
            #重复数字出现在前半段
                end = middle
            else:
            #出现在后半段
                start = middle + 1
        return -1
        """
        
        #用原表模拟哈希表
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            else:
                nums[abs(num)] = -nums[abs(num)]
                #给已找到的元素做标注