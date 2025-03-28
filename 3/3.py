class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        #dic保存的不是窗口内所有元素，而是出现过的元素最右位置
        i=-1
        res=0
        for j in range(len(s)):
            if s[j] in dic:
                i=max(dic[s[j]],i)
                #括号里的i是前一个存在相同项的元素的上一个出现位置，也就是无重复数组的开头，重复数字的下一位，dic是当前发现的相同项的元素的上一个出现位置
                #左面的i和dic[s[j]]的意义一样
                #max避免重复元素之间也有重复元素，使得左指针左移，比如abba，j到达第二个a时，i会从第一个b到第一个a
                
                #如果找到重复项，i从上一个位置变成当前相同项的前一个，更新dic储存当前相同项的另一个
                
            dic[s[j]]=j#入和改的操作都是这个
            #更新当前相同项的哈希表
            res=max(res,j-i)
            #因为结尾处不一定有相同字母，所以每次都要计算
        return res

#动态规划
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i
            dic[s[j]] = j # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res

#将问题转化为首次找到两个相同元素间的距离
#dic记录最后一次遇到某个元素的位置


#或者用哈希表一个一个检查