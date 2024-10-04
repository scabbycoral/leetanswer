class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        x, y, n, m = 0, 0, 0, 1
        for num in sockets:      # 1. 遍历异或
            n ^= num
        while n & m == 0:        # 2. 循环左移，计算 m，m是xy异或结果的倒数第一个1
            m <<= 1
        for num in sockets:      # 3. 遍历 sockets 分组
        #通过m位是否为1分为两组，因为相同数字肯定要么都是1要么都是0
        #下面的顺序可以互换，因为已经分组了
            if num & m:
                print('1',num)
                x ^= num # 4. 当 num & m != 0
            else:
                print('0',num)
                y ^= num       # 4. 当 num & m == 0
        return x, y              # 5. 返回出现一次的数字
