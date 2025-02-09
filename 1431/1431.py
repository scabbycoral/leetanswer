# Python file for number 1431 
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        k = max(candies)
        return [c + extraCandies >= k for c in candies]