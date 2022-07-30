
"""
    两两交换链表中的节点
    给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # 必须有pre的下一个和下下个节点才能交换, 否则说明交换已经结束的
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            # pre, cur, post对应左、中间、右节点
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return dummy.next