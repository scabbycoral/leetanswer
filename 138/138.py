#题目中入参node.random是位置index，但是实际参数是节点node，题目只是为了更清晰显示指向的位置

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        #哈希表
        if not head: return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
            #key是原节点，value是新节点
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            #这里用get而不是[]是因为有可能指向null，[]无法获得，get可以获得
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]
        """
        
#增长并分割
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
    #在每个旧节点后创建新节点，然后拆分
        if not head: return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = cur.next.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
                #新节点           旧节点
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        #pre保存原链表，cur保存复制链表
        while cur.next:
        #为什么不要从第12位开始而不是前面加入一个虚拟节点None并从这里开始，因为加入一个节点会导致pre需要比cur多一轮迭代，循环会提前停止
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
            #因为cur和pre已经next.next过了，所以直接等于下一个就好
        pre.next = None # 单独处理原链表尾节点
        #第3部分可以不用拆分，直接对cur进行next.next即可
        return res      # 返回新链表头节点
        
        
#next和random同时递归

class Solution:
    def __init__(self):
        self.cachedNode = {}  # 哈希表缓存
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None  # 如果原链表为空，直接返回空

        # 如果当前节点未被缓存，则创建新节点
        if head not in self.cachedNode:
        #这个if负责剪枝，避免已经从next读入的分支又要从random读取一遍
            headNew = Node(head.val)  # 创建新节点
            self.cachedNode[head] = headNew  # 缓存当前节点
            # 递归复制 next 和 random 指针
            headNew.next = self.copyRandomList(head.next)
            headNew.random = self.copyRandomList(head.random)

        return self.cachedNode[head]  # 返回缓存中的新节点
        
        
#next递归，因为next全部执行结束所有节点都已经被记录，在回溯的时候记录random则不需要剪枝
class Solution:
    def __init__(self):
        self.cachedNode = {}  # 哈希表缓存
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        headNew = Node(head.val)
        self.cachedNode[head] = headNew
        headNew.next = self.copyRandomList(head.next)
        headNew.random = self.cachedNode[head.random] if head.random else None

        return self.cachedNode[head]  # 返回缓存中的新节点