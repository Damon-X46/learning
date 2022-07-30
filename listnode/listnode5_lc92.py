"""
    反转链表II
    给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
    请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        # 两次遍历(找到left和right要遍历一次，反转要遍历一次)

        # 反转链表
        def reverse_linked_list(head):
            pre = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # 第一步：走到left节点的前一个节点
        for _ in range(left - 1):
            pre = pre.next
        
        # 第二部：来到right节点
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next
        
        # 第三步：切割出一个子链表
        left_node = pre.next
        post = right_node.next
        pre.next = None
        right_node.next = None

        # 第四步：反转链表
        reverse_linked_list(left_node)

        # 第五步：接回到原来的链表中
        pre.next = right_node
        left_node.next = post
        return dummy.next


        # 一次遍历
        # dummy= ListNode(0)
        # dummy.next = head
        # pre = dummy
        # for i in range(left - 1):
        #     pre = pre.next
        # cur = pre.next
        # for i in range(left, right):
        #     post = cur.next
        #     cur.next = post.next
        #     post.next = pre.next      # 注意这里不是post.next = cur
        #     pre.next = post
        # return dummy.next