class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k=min(len(nums1),len(nums2))
        i=j=0
        new=[]
        l=len(nums1)+len(nums2)
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]:
                new.append(nums2[j])
                j+=1
            else:
                new.append(nums1[i])
                i+=1
            if len(new)==l/2+1 and l%2==0:
                return (new[-1]+new[-2])/2
            if len(new)==l/2 and l%2!=0:
                return new[-1]
            #合并的时候如果合并列表比两个列表的长度和的一半长，则说明new里已经包含了中位数
        #也有可能有一个链表太小了，没包含有意义的数据，需要完全合并之后
        new+=nums1[i:] if j==len(nums2) else nums2[j:]
        return (new[len(new)//2]+new[len(new)//2-1])/2 if len(new)%2==0 else new[len(new)//2]
        #复杂度m+n
        
        `
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            #此函数的意义是寻早第k小的元素
            
            index1, index2 = 0, 0
            #下标移动后的左边界，因为当找到更小的数时，比他还小的数就没用了
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                    #当前情况表示下标超过了右边界，说明nums1里的数全都小于nums2的当前项并且还没到k
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                    #因为是有序数组，当k为1，说明当前项都是修改过后两个数组中的最小值，间接说明已经去掉了k-1个小的数字

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                #避免越界，如果越界，则取最右边界
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    #k要减去比当前项小的数的数量
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

#复杂度log(m+n)