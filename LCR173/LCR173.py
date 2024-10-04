class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        i, j = 0, len(records) - 1
        while i <= j:
            m = (i + j) // 2
            if records[m] == m: i = m + 1
            else: j = m - 1
        return i
