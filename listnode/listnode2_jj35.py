
# 不是很懂
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # 复制各节点，并建立“原节点->新节点”的map映射
        adict = {}
        cur = head
        while cur:
            adict[cur] = Node(cur.val)
            cur = cur.next

        # 构建新节点的next和random指向
        cur = head
        while cur:
            adict[cur].next = adict.get(cur.next)
            adict[cur].random = adict.get(cur.random)
            cur = cur.next
        return adict[head]      # 返回新链表头节点

node1, node2, node3, node4, node5 = Node(7), Node(13), Node(11), Node(10), Node(1)
node1.next, node1.random = node2, None
node2.next, node2.random = node3, node1
node3.next, node3.random = node4, node5
node4.next, node4.random = node5, node3
node5.next, node5.random = None, node1

aaa = Solution()
bbb = aaa.copyRandomList(node1)
print(bbb.val, bbb.next.val)