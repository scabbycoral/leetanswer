class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - len(nums) + len(small))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot
        
        return quick_select(nums, k)
#O(nlogn)



class Solution:
    def findKthLargest(self, nums, k):
    # Create a bucket array with size 20001 to handle the range -10000 to 10000
        buckets = [0] * 20001

    # Fill the buckets based on the nums array
        for num in nums:
            buckets[num + 10000] += 1

    # Traverse the bucket array from the highest index to the lowest
        for i in range(20000, -1, -1):
            k -= buckets[i]
            if k <= 0:
                return i - 10000

    # Return statement to handle unexpected cases, although it should never be reached
        return 0
#O(n)
#顺序表，按照顺序表保存的每个元素个数进行k-，只需要知道k<=0的一段位置之一即可，因为这段保存的数据一样