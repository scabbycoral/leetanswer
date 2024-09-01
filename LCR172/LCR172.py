class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        # 搜索右边界 right
        i, j = 0, len(scores) - 1
        while i <= j:
            m = (i + j) // 2
            if scores[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and scores[j] != target: return 0
        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if scores[m] < target: i = m + 1
            else: j = m - 1
        left = j
        return right - left - 1
