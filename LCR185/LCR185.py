class Solution:
    def statisticsProbability(self, num: int) -> List[float]:
        dp = [1 / 6] * 6
        for i in range(2, num + 1):
            tmp = [0] * (5 * i + 1)
            #保存点数和，因为比i小的肯定取不到
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j + k] += dp[j] / 6
            #从上一个结果dp找一个映射到下一个结果
            dp = tmp
        return dp

#逆向是指从n-1的x个结果，每次计算一个n的x的其中一个结果
#正向是指将n-1的结果同时放入可能影响到的n的6个x中，像金字塔一样摞起来
"""
import torch.nn.functional as F
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        # 初始化单个骰子的概率分布
        single_dice_prob = torch.tensor([1.0 / 6] * 6).view(1, 1, 6)
        # 初始情况，只有一个骰子
        n_dice_prob = torch.tensor([1.0 / 6] * 6).view(1, 1, 6) 
        for _ in range(n - 1):
            # 更新概率分布
            n_dice_prob = F.conv1d(n_dice_prob, single_dice_prob, padding=5).view(1, 1, -1)
        return n_dice_prob.squeeze()

"""