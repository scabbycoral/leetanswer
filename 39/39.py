from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                res.append(list(path))
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # 选择当前元素
                backtrack(i, path, remaining - candidates[i])  # 允许重复选择
                path.pop()  # 撤销选择

        backtrack(0, [], target)
        return res
