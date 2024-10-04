class Solution:
    def dismantlingAction(self, arr: str) -> str:
        hmap={}
        for i in arr:
            if i not in hmap:
                hmap[i]=False
            else:
                hmap[i]=True
        print(hmap)
        for i in hmap.keys():
            if not hmap[i]:
                return i
        return ' '
        
#有序哈希表
class Solution:
    def dismantlingAction(self, arr: str) -> str:
        hmap = collections.OrderedDict()
        for c in arr:
            hmap[c] = not c in hmap
        for k, v in hmap.items():
            if v: return k
        return ' '
#目前{}就是有序的