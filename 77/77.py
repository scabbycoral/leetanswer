class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, path = [], []
        self.dfs(n, k, 1, path, result)
        return result

    def dfs(self, n, k, start, path, result):
        if k == 0:
            result.append(path[:])
            return
        for i in range(start, n-k+2):
            path.append(i)
            self.dfs(n, k-1, i+1, path, result)
            path.pop()
            
#和全排列不同，这个题考验的是选择并排列，47的全排列是交换并排列

"""
#不剪枝
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, track = [], []
        self.backtrack(n, k, 1, track, result)
        return result

    def backtrack(self, n, k, start, track, result):
        if len(track) == k:
            result.append(track[:])
        for i in range(start, n+1):
            track.append(i)
            self.backtrack(n, k, i+1, track, result)
            track.pop()
"""