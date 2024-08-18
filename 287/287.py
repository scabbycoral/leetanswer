class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        """
        #方法一，哈希表
        hmap=set()
        for i in documents:
            if i in hmap:
                return i
            hmap.add(i)
        return
        """
        #方法二，静态表
        i=0
        while i<len(documents):
            if documents[i]==i:
                i+=1
                continue
                #位置正确且没冲突，继续找下一个
            elif documents[i]==documents[documents[i]]:
                return documents[i]
                #位置不正确且冲突返回重复值
            else:
                documents[documents[i]],documents[i]=documents[i],documents[documents[i]]
                #位置不正确且不冲突则交换位置
        return -1


