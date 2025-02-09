class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, tmp = [1] * len(nums), 1
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1] # 下三角
        print(ans)
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]                # 上三角
            ans[i] *= tmp                     # 下三角 * 上三角
        return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, l, r = [1] * len(nums), 1, 1
        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i], l = res[i] * l, l * nums[i]
            res[j], r = res[j] * r, r * nums[j]
            print(res,l,r)
        return res

#左右乘积列表
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L,R=[1],[1]
        for i in range(1,len(nums)):
            L.append(L[i-1]*nums[i-1])
        for i in reversed(range(len(nums)-1)):
            R.insert(0,R[0]*nums[i+1])
        ans=[]
        for i in range(len(L)):
            ans.append(L[i]*R[i])
        return ans