class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        candidates.sort()
        self.DFS(candidates,target,0,[],res)
        return res
    def DFS(self,nums,target,index,path,res):
        #每次从上一个位置开始往后加入path
        for i in range(index,len(nums)):
        #res和path每次都要往下一层传，所以放在参数里
        #加上个判断省去深度遍历
            if nums[i] > target:
                break
            if nums[i] == target:
                res.append(path+[nums[i]])
                return
            self.DFS(nums,target-nums[i],i,path+[nums[i]],res)
