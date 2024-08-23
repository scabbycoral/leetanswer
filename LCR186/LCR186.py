class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        unknown = 0
        places.sort() # 数组排序
        for i in range(4):
            if places[i] == 0: unknown += 1 # 统计未知朝代数量
            elif places[i] == places[i + 1]: return False # 若有重复，提前返回 false
        return places[4] - places[unknown] < 5 # 最大编号朝代 - 最小编号朝代 < 5 则连续
#为什么<5就可以，因为已经按照从小到大排序，0肯定用来弥补中间空缺，并且0一定不是当最小的数，这样空缺会更大，所以只要最大牌最小牌之间小于牌的数量，则一定可以连续
#没必要对本题排序
#这个题应该有一个前提，抽不到重复的牌