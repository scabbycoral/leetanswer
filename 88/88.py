# Python file for number 88 
#method.1
#把0全都替换成有效数字然后排序

#从后向前的双指针
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
                print(1,nums1)
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
                print(2,nums1)
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
                print(3,nums1)
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
                print(4,nums1)
            tail -= 1