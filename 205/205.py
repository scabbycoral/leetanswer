
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for a, b in zip(s, t):
            # 对于已有映射 a -> s2t[a]，若和当前字符映射 a -> b 不匹配，
            # 说明有一对多的映射关系，则返回 false ；
            # 对于映射 b -> a 也同理
            if a in s2t and s2t[a] != b or \
               b in t2s and t2s[b] != a:
               #必须是双向单射才能保证一一映射
                return False
            s2t[a], t2s[b] = b, a
        return True
#本题只需要保证唯一映射即可，因为同一个字符不可以映射到第二个字符