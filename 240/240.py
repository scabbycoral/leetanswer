class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        i,j=len(plants)-1,0
        while i>=0 and j<len(plants[0]):
            if plants[i][j]>target:i-=1
            elif plants[i][j]<target:j+=1
            else: return True
        return False